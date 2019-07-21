from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage

from fair.models import Fair
from companies.models import Company
from register.models import SignupLog
from accounting.models import Order

# This app is used to test functionality in production without making it accesible via the rest of the site (only via the url).

def testpage(request):

    print('Testpage view')

    return render(request, 'testpage/testpage.html')


def send_test_email(request):

    print('Testpage send email view function')

    company = get_object_or_404(Company, name='Test 2')
    fair = get_object_or_404(Fair, year=2019)

    signature = SignupLog.objects.filter(company = company, contract__fair = fair, contract__type = 'COMPLETE').first()
    # orders = Order.objects.filter(purchasing_company = company, unit_price = None, name = None)
    # orders_total = 10000 # dummy

    orders = []
    orders_total = 0

    for order in Order.objects.filter(product__revenue__fair = fair, purchasing_company = company):
        unit_price = order.product.unit_price if order.unit_price is None else order.unit_price
        orders_total += order.quantity * unit_price

        orders.append(
		{
			'category': order.product.category.name if order.product.category else None,
			'name': order.product.name if order.name is None else order.name,
			'description': order.product.description if order.product.registration_section is None else None,
			'quantity': order.quantity,
			'unit_price': unit_price
		})

    send_CR_confirmation_email(signature, orders, orders_total)

    return render(request, 'testpage/testpage.html')


def send_CR_confirmation_email(signature, orders, orders_total):
    print(orders)
    order_table_rows = []

    for order in orders:
        if order['category']:
            product = order['category'] + ' - ' + order['name']
        else:
            product = order['name']

        order_row = '''
						<tr>
						<td>%s</td>
						<td>%s</td>
						<td>%s</td>
						<td>%s</td>
						</tr>
					''' % (product, order['quantity'], order['unit_price'], str(int(order['quantity'])*int(order['unit_price'])))
        order_table_rows.append(order_row)

    html_message = '''
		<html>
			<head>
				<title></title>
			</head>
			<body>
				<style>
					* {
					  font-family: sans-serif;
					  font-size: 12px;
					}
				</style>
				<div>
					Thank you for submitting the complete registration for THS Armada 2019. The complete registration contract was signed by %s on the %s for %s.
					<br/><br/>
					Please note that this is an automatically generated email. If you have any questions please contact your sales contact person. For contact information, please visit our <a href="https://armada.nu/contact/">website</a>.
				</div>
				<div>
					<br/>
					To view or update your choices visit your <a href="http://ais.armada.nu/register/%s/registration">registration page</a>.
					<br/>
					Your current order contains the products listed below.
					<br/>
					Total price: SEK %s
					<br/><br/>
					<table align="left" border="1" cellpadding="1" cellspacing="0" style="width:600px">
						<thead>
							<tr>
								<th scope="col">Product</th>
								<th scope="col">Quantity</th>
								<th scope="col">Unit price (SEK)</th>
								<th scope="col">Total price (SEK)</th>
							</tr>
						</thead>
						<tbody>
							%s
						</tbody>
					</table>
				</div>
			</body>
		</html>
		''' % 	(
				str(signature.company_contact),
				str(signature.timestamp),
				str(signature.company),
				str(signature.company.pk),
				str(orders_total),
				''.join(order_table_rows),
				)

    email = EmailMessage(
		subject = 'Registration for THS Armada 2019',
		body = html_message,
		from_email = 'info@armada.nu',
		to = [signature.company_contact.email_address],
		# bcc = [],
	)
    email.content_subtype = 'html'

	# file_path = 'https://ais.armada.nu' + signature.contract.contract.url
	# print("Contract path: ", file_path)
	# email.attach_file(signature.contract.contract.url)
    email.send()
