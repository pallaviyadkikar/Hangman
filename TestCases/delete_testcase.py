
from validations import delete_validations

'''positive test cases'''
print("positive test cases")
print("input:movies,Expected Output:True");
print("Original Output:",delete_validations.validate_category("movies"));

'''positive test cases'''
print("positive test cases")
print("input:country,Expected Output:True");
print("Original Output:",delete_validations.validate_category("country"));


'''negative test cases'''
print("negative test cases")
print("input:city,Expected Output:False");
print("Original Output:",delete_validations.validate_category("city"));

'''positive test cases'''
print("positive test cases")
print("input:easy,Expected Output:True");
print("Original Output:",delete_validations.validate_level("easy"));

'''positive test cases'''
print("positive test cases")
print("input:medium,Expected Output:True");
print("Original Output:",delete_validations.validate_level("medium"));

'''positive test cases'''
print("positive test cases")
print("input:hard,Expected Output:True");
print("Original Output:",delete_validations.validate_level("hard"));

'''negative test cases'''
print("negative test cases")
print("input:large,Expected Output:False");
print("Original Output:",delete_validations.validate_level("large"));
