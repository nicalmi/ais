from django.forms import Select,  Form, ModelChoiceField, HiddenInput
from django import forms

from fair.models import Fair
from orders.models import Product, Order, ProductType, StandArea


class SelectStandAreaForm(Form):
    stand_area = forms.ModelChoiceField(queryset=StandArea.objects.filter(fair=Fair.objects.filter(current=True).first()))
    #def __init__(self, *args, **kwargs):
        #super(SelectStandArea, self).__init__(*args, **kwargs)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, exhibitor, *args, **kwargs):
        instance = kwargs.get('instance')
        super(OrderForm, self).__init__(*args, **kwargs)
        if instance == None:
            self.fields['exhibitor'].initial = exhibitor.pk
            self.fields['amount'].initial = 1
        self.fields['exhibitor'].disabled = True #make sure exhibitor field is not editable
        self.fields['amount'].disabled = True #make sure exhibitor field is not editable
        self.fields['exhibitor'].widget= HiddenInput()
        self.fields['amount'].widget= HiddenInput()

class OrderSelectionForm(OrderForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, exhibitor, product_type, *args, **kwargs):
        super(OrderSelectionForm, self).__init__(exhibitor,*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(product_type=product_type, display_in_product_list=True)
        
class OrderCheckboxForm(OrderForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, exhibitor, product, *args, **kwargs):
        instance = kwargs.get('instance')
        super(OrderCheckboxForm, self).__init__(exhibitor,*args, **kwargs)
        self.fields['add'] = forms.BooleanField(initial=False, required=False)
        self.fields['add'].label = product.name + str(product.price)
        self.fields['add'].help_text = product.description
        self.fields['add'].widget = forms.CheckboxInput()

        if instance == None:
            self.fields['product'].initial = product.pk
        else:
            self.fields['add'].initial = True

        self.fields['product'].disabled = True 
        self.fields['product'].widget = HiddenInput() 
        
    def save(self, commit=False):
        if self.cleaned_data['add'] == True:
            super(OrderCheckboxForm, self).save(commit=True)
        else:
            # Try to delete previous order if existing
            try:
                prev_order = Order.objects.filter(exhibitor=self.cleaned_data['exhibitor'], product=self.cleaned_data['product']).first()
                prev_order.delete()
            except: 
                pass

class OrderAmountForm(OrderForm):
    def __init__(self, exhibitor, product, *args, **kwargs):
        instance = kwargs.get('instance')
        super(OrderAmountForm, self).__init__(exhibitor, *args, **kwargs)
        self.fields['amount'].disabled = False
        self.fields['amount'].widget = forms.NumberInput()
        self.fields['amount'].help_text = product.description
        self.fields['amount'].label = product.name
        if instance == None:
            self.fields['product'].initial = product.pk
            self.fields['amount'].initial = 0
        self.fields['product'].disabled = True 
        self.fields['product'].widget = HiddenInput() 


def get_order_forms(exhibitor, product_type, *args, **kwargs):
    """
        Returns a list of order forms. Given the product type, the orderforms could be 
        a select one field or select multiple field, together with an amount field or not. 
        A product type with selection_policy == 'SELECT' will return a form with one ChoiceField
        where the choices are the products that has that product type.
    """
    if product_type.selection_policy == 'SELECT':
        kwargs['instance'] = Order.objects.filter(exhibitor=exhibitor, 
                product__in=Product.objects.filter(product_type=product_type, display_in_product_list=True)).first()
        return [OrderSelectionForm(exhibitor, product_type, *args, **kwargs)]
    else:
        order_forms = []
        products = Product.objects.filter(product_type=product_type, display_in_product_list=True)
        for i, product in enumerate(products):
            kwargs['instance'] = Order.objects.filter(exhibitor=exhibitor, product=product).first()
            kwargs['prefix'] = kwargs['prefix'] + str(i)
            if product_type.selection_policy == 'SELECT_MULTIPLE':
                order_forms.append( OrderCheckboxForm(exhibitor, product, *args, **kwargs))
            else:
                order_forms.append( OrderAmountForm(exhibitor, product, *args, **kwargs))
        return order_forms


