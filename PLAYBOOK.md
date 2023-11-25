# MIS ProBono

## Introduction
As part of the MIS ProBono project we have learned the Reach to Teach team is looking for a solution that would help them and government officials of different states to make better decisions and have a more thorough understanding of what is happening in the "field". For example, common queries are:
- "How many schools are there in a given state?"
- "How many boys and girls are in a particular school?"
- "How many boys and girls are in a particular grade?"
- etc

After several discussions with Reach to Teach team it became clear that while initially we were talking about dashboards and visualizations, it became apparent that they are looking for help in building a Data Management solution. As far as as we were able to observe, the data is currently stored in Excel files and is not easily accessible. The goal of this project is to build a solution that would allow Reach to Teach team to easily access the data and answer the questions they have.

## Data Management platform - WIP
While talking to Reach to Teach team we have identified that they are thinking in terms of use cases. One of the first things when trying to use any system is to be able to provide an organization mode that would make sense for the users of the system. Reach to Teach team have access to PowerBI and after several explorations we have decided to use PowerBI as a platform for the Data Management solution. The main reason for this is that PowerBI is already used by Reach to Teach team, they have access to it at no additional cost and they are familiar with it.

A few assumptions that we are making regarding Reach to Teach team access to Microsoft technologies:
- Access to Active Directory - this will be used for user and access management
- Access to PowerBI Service - this will be used for data upload, reports, dashboards, etc

At a very high level any use case would go through the following flow:
1. Create a PowerBI workspace - a workspace is a container for datasets, tables, dashboards, reports for a particular use case. One nice feature of PowerBI workspaces is that it allows you to assign roles to users and control who has access to the workspace. The assumption here is that we already know the users and roles.
2. Create a semantic model aka datasets and tables - to be able to make sense of the data that has to be analyzed it is necessary to create a semantic model. A semantic model would consist of one or more datasets along with the associated tables. An important step at this stage is identifying which tables are dimension/lookup table and which ones are fact tables. Ideally the semantic model should be created and stored in a format that is usable from a Git repo. For example using something like YAML or JSON. This would allow us to track changes to the semantic model and also allow us to use the same semantic model in different workspaces.
3. Create input, output, error folders - these input folder will be used to store the raw input Excel/CSV files, the output folder will be used to store files in the standard format and the error folder will be used to store files that have errors and might need reprocessing. To make things easier these folder names should be derived from the workspace name, so it is easier to identify which folders belong to which workspace.
4. Create/reuse ETL jobs - having the semantic model and the input, output, error folders it is possible to create ETL jobs that would read the input files, transform them, store them in the output folder and then upload data to PowerBI. The ETL jobs should be created in a way that they can be easily reused in different workspaces. For example, the ETL jobs should be stored in a Git repo and should be parameterized so that they can be easily reused in different workspaces.
5. Create PowerBI reports/dashboards/apps - once the data flow has been configured and data is continuously flowing into PowerBI, analysts can create reports, dashboards, etc for final consumption.

### Use case management in PowerBI

#### Workspace creation
As it was mentioned previously, a use cases will be mapped to a PowerBI workspaces. To make sure that everything is properly configured and secured from PowerBI perspective the use case project owner should ensure that the following steps are completed:
1. Use case has a PowerBI workspace
2. Use case has an Active Directory user group
3. User group is assigned to the workspace
4. Users within the user group are assigned to the workspace with the appropriate role

#### Semantic model creation
To make sense of data, a semantic model is a must. While it might sound like a lot of work, a semantic model can be easily derived from the Excel files that will be uploaded for a particular use case.

The whole process of creating a semantic model can be broken down into the following steps:
1. Use case is using an Excel file that self contained and using a single sheet? - if the uploaded file has all the data, then the semantic model can be as simple as creating a dataset with a table that contains the Excel sheet columns. It should be noted that ideally the semantic model table columns should follow some standard naming convention. For example, if the Excel sheet has a column named "School Name", then the semantic model table column should be named "school_name". This will make it easier to reference the columns in the semantic model.
2. Use case is using an Excel file that is self contained and using multiple sheets? - if the uploaded file has all the data and it contains multiple sheets, then the semantic model should have a dataset with multiple tables. Each table should correspond to a sheet in the Excel file. The table columns should follow the same naming convention as in the previous step.
3. Use case is using multiple files? - if the use case is using multiple files, then the semantic model should can contain one or more datasets and depending on Excel file structure like one or more sheets each dataset can contain one or more tables. The table columns should follow the same naming convention as in step 1. In general when dealing with a use case based on multiple files each file should be analyzed and a decision should be made whether it makes sense to have a single dataset with multiple tables or multiple datasets with one or more tables. The decision should be based on the data and the use case requirements.

While working on semantic model it is critical to make sure that the model is explicit about which tables a dimension/lookup tables and which tables are fact tables. This should help the ETL jobs to properly process the data and avoid unnecessary work when dealing with dimension/lookup tables.

While not strictly related to semantic model creation in PowerBI, we should make sure that the mapping from Excel files sheets to semantic model dataset name and table columns is stored in a place that can be easily accessed and used by the ETL jobs.

#### ETL jobs creation
Currently this is a big unknown. It is unclear if Reach to Teach team has an existing IT system in place. Is there anything that can be deployed on-prem, could we propose using something like Azure and some of the relevant services.

Another area that needs some clarification if there is a preferred programming language that should be used for the ETL jobs. During one of our discussions it was mentioned that Python is a preferred language, but it is not clear if this is a hard requirement or just a preference.
