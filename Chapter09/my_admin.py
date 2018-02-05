from Admin import Admin
adm_user = Admin('Muhammad', 'Ali', 'Islam', 22, 'Karachi')
print(adm_user.describe_user())  # print the user method which is defined in parent class
adm_user.prvl_list.show_privileges()  # print the method 'show_privileges()' that will show rights of admin(defined in a list)
