def make_profile(first, last , **user_info):
    profile = {}
    profile['First Name'] = first
    profile['Last Name'] = last
    for ab , cd in user_info.items():
        profile[ab] = cd
    return profile
profile  = make_profile('Muhammad ' , 'Umer' , Religion = 'Islam' , Age = 22 , City = 'Karachi' , Country = 'Pakistan')
print(profile)