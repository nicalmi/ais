def callback(tree):
    username = tree[0][0].text
    user, user_created = User.objects.get_or_create(username=username)
    if user_created:
        #add email
        user.save()
        pass
        