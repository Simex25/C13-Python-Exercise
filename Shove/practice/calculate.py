from Shove.practice.classes import FirstClass

# In[2]: print("welcome to python")
# In[4]: print("Python")

if __name__ == '__main__':
    result = FirstClass("C_Thirteen", 2)
    print(result.get_name())
    result.set_age('30')
    print("my age is: ", result.get_age())
