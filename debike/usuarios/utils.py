def save_user(form):
    user = form.save(commit=False)
    user.first_login = False
    user.save()
