eastboundtraffic=False
westboundtraffic=True

def check(eastboundtraffic, westboundtraffic):
    if type(eastboundtraffic) != bool or type(westboundtraffic) != bool:
        print("Error")
    if eastboundtraffic == westboundtraffic:
        print("False")
    else:
        print("True")