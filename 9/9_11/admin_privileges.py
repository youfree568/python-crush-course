import user

main_admin = user.Admin("Nick", "Brokowich", 33, "nick@mail.com")

main_admin.privileges.show_privileges()
main_admin.privileges.privileges = ['can add comment', 'can ban user', 'can unban user', 'can delete user']
main_admin.privileges.show_privileges()