street = "Gardener"
neighborhood = "Sogbon"
district = "Bodomzor"
region = "Samarkand"

print (street + "street," + neighborhood + "neighborhood," + \
      district + "district," + region + "region")

print ("Please enter the following information:")
street = input ("Street:")
neighborhood = input ("Your neighborhood:")
district = input ("Your district:")
region = input ("Your region:")
print (street + "street," + neighborhood + "neighborhood," + \
      district + "district," + region + "region")

print (street + "street, \ n" + neighborhood + "neighborhood, \ n" + \
      district + "district, \ n" + region + "region")

address = f"{street} street, {neighborhood} neighborhood, {district} district, {region} region"
print (address)

print (address.upper ())
print (address.lower ())
print (address.title ())
print (address.capitalize ())