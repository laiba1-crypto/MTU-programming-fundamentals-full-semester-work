#Author : Laiba Asif
#Purpose : Project Job


#number of job user inputs
num_of_job = str(input("Enter number of jobs : "))

#converting number of jobs to integer
jobs = int(num_of_job)
i=1

#job list created to gather info from user
job = []

# while loop is used to run through the program
while jobs >= i:
 
    
    n=0

    print("Enter the details of job",i)
    print("-" *34)

    #User Input job title
    job_title = str(input("What is the Job Title : "))
    
    #User Input company name
    name_of_company = str(input("What is the Company Name : "))
    
    #User Input employment type
    print("Please Specify the type of employment")
    type_of_employment= str(input("1: PartTime \n2: FullTime \n ==> "))
    
        
    if type_of_employment=='1' :
        type_of_employment = "Part-Time"
        no_of_hour=input("Enter number of hours worked : ")
        hour=int(no_of_hour)
            
    elif type_of_employment=='2' :
        type_of_employment = "Full-Time"
        no_of_hour='40';
        hour=int(no_of_hour)
        
    else :
        print ("Please choose valid option")
           
    #User Input job experience requirement    
    experience = str(input("Does the job requires experience (y/n) "))
   
    #User Input Rate per hour paid
    rate = input("Enter rate paid per hour : ")
    
    #convert to integer
    rate1=int(rate)
    
    #Calculate total earning
    earning = hour*rate1
    
    #conver earning to string
    earning2=str(earning)
    
    #k is an object that will be appended in job
    k=(i , job_title , name_of_company,experience,rate,no_of_hour,earning2)
    
    #appended k object to job list
    job.append(k)
    
    #if else used here to determibne which file to open and write into it
    if hour<=39:
        #file opened
        file2 = open('part-time.txt','a')
        #writing in file
        file2.write(str(i))
        file2.write(" ")
        file2.write(job_title)
        file2.write("\n")
        file2.write(name_of_company)
        file2.write(" ")
        file2.write(experience)
        file2.write(" ")
        file2.write(rate)
        file2.write(" ")
        file2.write(no_of_hour)
        file2.write(" ")
        file2.write(earning2)
        file2.write("\n")
        #file closed
        file2.close()
    elif hour>39:
        #file opened
        file1 = open('full-time.txt','a')
        #writing in file
        file1.write(str(i))
        file1.write(" ")
        file1.write(job_title)
        file1.write(" ")
        file1.write(name_of_company)
        file1.write(" ")
        file1.write(experience)
        file1.write(" ")
        file1.write(rate)
        file1.write(" ")
        file1.write(no_of_hour)
        file1.write(" ")
        file1.write(earning2)
        file1.write("\n")
        #file closed
        file1.close()
        
    i=i+1
 
    

print("Id JOBTITLE LOCATION EXP RATE(€) HOURS EARNINGS")
print("=="*24)

#For loop used to get all values in job list
for jobs in job:
    x=1
    #tried using f-string but was overwritting object in list
    #jobs=f'{x}.  {job_title:8} {name_of_company:8} {experience:4} {rate:5}  {no_of_hour:7} {earning:5}'
    print(jobs)
    x=x+1

       
    
       