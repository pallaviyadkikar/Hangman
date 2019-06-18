from validations.Validation_Package import confirm_password
from validations.Validation_Package import change_new_password

'''positive test cases'''
print("Positive Test Cases");
print("input:jeev,Expected Output:True");
print("Original Output:",confirm_password("jeev"));
'''Negative test cases'''
print("Negative Test Cases");
print("input:jenil,Expected Output:False");
print("Original Output:",confirm_password("jenil"));
'''positive test cases'''
print("Positive Test Cases");
print("input:jenil,jenil,Expected Output:True");
print("Original Output:",change_new_password("jenil","jenil"));
'''Negative test cases'''
print("Negative Test Cases");
print("input:jenil,jeev,Expected Output:False");
print("Original Output:",change_new_password("jenil","jeev"));