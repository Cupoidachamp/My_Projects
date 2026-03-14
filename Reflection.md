### **Reflection**



1. ##### **Biggest Surprise**



The biggest surprise during this assignment was how interconnected AWS services are, even for a relatively small pipeline. I initially expected the process to involve only copying a file between S3 folders, but it required configuring IAM roles, permissions, Glue jobs, and ensuring services like Redshift and Glue could communicate with each other properly. This helped me understand how important correct permissions and service integration are in cloud data workflows.



##### **2. Challenge Faced and Solution**



One challenge I encountered was related to permissions and schema mismatches when querying the data. At one point, Redshift could not access the Glue Data Catalog tables due to missing permissions, and later there was a Parquet schema incompatibility error. I resolved these issues by updating IAM role permissions to allow Glue access and adjusting the schema definition to match the actual data type written by Spark. Carefully reading the error messages and checking AWS documentation helped me troubleshoot the issues.



##### **3. When to Use Glue vs Athena vs S3-only**



Glue is best suited for automated ETL pipelines where data needs to be transformed or processed regularly. Athena is useful for quick, ad-hoc SQL queries directly on data stored in S3 without managing infrastructure. An S3-only approach works well for simple storage or file movement tasks where no data processing or querying is required.



