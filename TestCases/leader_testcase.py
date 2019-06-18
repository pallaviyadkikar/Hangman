from validations import validation_leader

'''positive test cases'''
print("positive test cases")
print("input:jeevan,Expected Output:True");
print("Original Output:",validation_leader.validate_name("jeevan"));

'''negative test cases'''
print("negative test cases")
print("input:jikku,Expected Output:False");
print("Original Output:",validation_leader.validate_name("jikku"));

'''positive test cases'''
print("positive test cases")
print("input:london,Expected Output:True");
print("Original Output:",validation_leader.validate_city("london"));

'''negative test cases'''
print("negative test cases")
print("input:india,Expected Output:False");
print("Original Output:",validation_leader.validate_city("india"));

'''positive test cases'''
print("positive test cases")
print("input:y,Expected Output:True");
print("Original Output:",validation_leader.validity_yesno("y"));


'''negative test cases'''
print("negative test cases")
print("input:n,Expected Output:False");
print("Original Output:",validation_leader.validity_yesno("n"));

'''positive test cases'''
print("positive test cases")
print("input:3,Expected Output:True");
print("Original Output:",validation_leader.validate_selection("3"));

'''positive test cases'''
print("positive test cases")
print("input:6,Expected Output:True");
print("Original Output:",validation_leader.validate_selection("6"));

'''negative test cases'''
print("negative test cases")
print("input:11,Expected Output:False");
print("Original Output:",validation_leader.validate_selection("11"));

'''positive test cases'''
print("positive test cases")
print("input:country,Expected Output:True");
print("Original Output:",validation_leader.validate_category("country"));

'''positive test cases'''
print("positive test cases")
print("input:movies,Expected Output:True");
print("Original Output:",validation_leader.validate_category("movies"));

'''negative test cases'''
print("negative test cases")
print("input:state,Expected Output:False");
print("Original Output:",validation_leader.validate_category("state"));




