name = 'Kristine'
product = 'Python elearning course'
email_content = f"""
Hi {name}
Thank you for purchasing {product}
Regards

Sales Team
"""

print(email_content)
# print(email_content.strip()) 
# Se puede usar .strip para quitar los caracteres en blanco y que todo quede más limpio.

name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Jordan'

greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Jordan')

greeting = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"
# más limpia y menos liosa la segunda opción: utilizar f y no el índice
print(greeting)