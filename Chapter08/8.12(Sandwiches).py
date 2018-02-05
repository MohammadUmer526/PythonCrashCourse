def make_sandiwches(*types):
    print("Making sandwiches with following flavor:")
    for type in types:
        print("-" + type)
make_sandiwches('checiken','veetable','club sandwiches')
make_sandiwches('simple')
make_sandiwches('BBQ')