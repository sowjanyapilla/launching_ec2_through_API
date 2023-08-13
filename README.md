# launching_ec2_through_API
**Prerequisites:**

1.**AWS Account**: You need an active AWS account to create and manage Lambda functions, EC2 instances, and API 
  Gateway.
  
2.**GitHub Repository:** Have a GitHub repository containing the necessary code for launching an EC2 instance. This 
   could be in the form of a CloudFormation template or a script that utilizes AWS SDKs.

3.**AWS CLI:** Install and configure the AWS Command Line Interface (CLI) to interact with AWS services from your local machine.

**Setup Steps**

**1. Clone GitHub Repository**
Clone your GitHub repository containing the code/scripts required to launch an EC2 instance.

**you can use these commands to clone :**
  git clone <repository_url>
  cd <repository_directory>

**2. Create Lambda Function**
  1.Open the AWS Management Console.
  
  2.Navigate to the Lambda service.
  
  3.Click "Create Function."
  
  4.Choose "Author from scratch":
  
  5.Function name: Choose a name for your Lambda function.
  
  6.Runtime: Select the appropriate runtime for your code (e.g., Python, Node.js, etc.).
  
  7.In "Function code," either upload a ZIP file containing your code or directly copy-paste the code.
  Under "Basic settings," increase the timeout based on your code's execution time.
  
  8.Click "Create Function."
  
**3. Configure Lambda Trigger**
  
  1.In the Lambda function's configuration, click "Add trigger."
  
  2.Select "API Gateway" as the trigger type.
  
  3.Choose "Create an API" and configure the API:
  
  4.Security: Open or secure the API based on your requirements.
  
  5.API type: Choose "HTTP API."
  
  6.Click "Add."
  
**4. Set Up API Gateway**
  
  1.In the AWS Management Console, navigate to API Gateway.
  
  2.Select the API you created in the previous step.
  
  3.Under "Routes," click "Create" and define a resource and method (e.g., POST).
  
  4.Configure the integration type as "Lambda Function" and select your Lambda function.
  
  5.Deploy the API to create a live endpoint.
  
**5. Grant Lambda Permissions**
    The Lambda function requires permissions to launch EC2 instances. Create an IAM role with appropriate 
  permissions and attach it to the Lambda function.

**6. Test the Setup**
click on the link generated by API and at end add resource,created in API  The Lambda function will be triggered, and it should execute the code to launch an EC2 instance.

**Conclusion**
You have successfully set up a system that launches an EC2 instance by triggering a Lambda function using an API This architecture allows for automated infrastructure provisioning based on API requests.

Remember to follow best practices for security, IAM roles, and code deployment when implementing this setup in a production environment.









