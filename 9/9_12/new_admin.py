from admin_and_privileges import Admin, Privileges

new_admin = Admin("Nick", "Smith", 33, "smith@mail.com")

new_admin.describe_user()

new_admin.privileges.privileges = ["can say: fffffffff"]
new_admin.privileges.show_privileges()