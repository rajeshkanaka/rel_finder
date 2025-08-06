# https://ezekia.com/api/documentation llms-full.txt

## Ezekia API Documentation
Explore

## Ezekia  ```  2.1.1  ```    ``` OAS 3.0 ```

[https://ezekia.com/docs/api-docs.json](https://ezekia.com/docs/api-docs.json)

### Software for Search Firms

Intuitive, easy to use, fast and customizable

[Terms of service](https://ezekia.com/#/terms/subscription-agreement)

[Contact the developer](mailto:support@ezekia.com)

Servers

https://ezekia.com/api

Authorize

### People (Profile)

GET
/people

Fetches all people.

POST
/people

Creates a person.

GET
/people/{id}

Fetches a person by ID.

PUT
/people/{id}

Updates a person.

DELETE
/people/{id}

Deletes a person by ID.

GET
/v2/people

Fetches all people.

POST
/v2/people

Creates a person.

GET
/v2/people/{id}

Fetches a person by ID.

PUT
/v2/people/{id}

Updates a person.

DELETE
/v2/people/{id}

Deletes a person by ID.

GET
/v3/people

Fetches all people.

POST
/v3/people

Creates a person.

GET
/v3/people/{id}

Fetches a person by ID.

PUT
/v3/people/{id}

Updates a person.

DELETE
/v3/people/{id}

Deletes a person by ID.

### People (Confidential Details)

POST
/people/{personId}/confidential

Sets confidential details for a person

### People (Aspirations)

POST
/people/{personId}/aspirations

Sets aspiration details for a person

### People (Current Status)

POST
/people/{personId}/current-status

Sets current status for a person

### People (Emails)

POST
/people/{id}/emails

Adds a new email address to a person.

PUT
/people/{id}/emails/{emailId}

Updates an email address on a person.

DELETE
/people/{id}/emails/{emailId}

Deletes an email address from a person.

### People (Phones)

POST
/people/{id}/phones

Adds a new phone number to a person.

PUT
/people/{id}/phones/{phoneId}

Updates an phone number on a person.

DELETE
/people/{id}/phones/{phoneId}

Deletes an phone number from a person.

### People (Links)

POST
/people/{id}/links

Adds a new link to a person.

PUT
/people/{id}/links/{linkId}

Updates a link on a person.

DELETE
/people/{id}/links/{linkId}

Deletes a link on a person.

### People (Positions)

GET
/people/{personId}/positions

Gets all positions for a person

POST
/people/{personId}/positions

Creates a position for a person

PUT
/people/{personId}/positions/{positionId}

Updates a position for a person

DELETE
/people/{personId}/positions/{positionId}

Deletes a position for a person

GET
/v2/people/{personId}/positions

Gets all positions for a person

POST
/v2/people/{personId}/positions

Creates a position for a person

PUT
/v2/people/{personId}/positions/{positionId}

Updates a position for a person

DELETE
/v2/people/{personId}/positions/{positionId}

Deletes a position for a person

### People (Education/Qualifications)

GET
/people/{personId}/education

Gets all educations for a person

POST
/people/{personId}/education

Creates a education for a person

PUT
/people/{personId}/education/{educationId}

Updates an education for a person

DELETE
/people/{personId}/education/{educationId}

Deletes an education for a person

### People (Notes)

POST
/people/notes

Adds notes to one or more people.

PUT
/people/notes/{id}

Updates a note.

DELETE
/people/notes/{id}

Deletes a note.

### People (Lists)

GET
/lists/{id}/people

Fetches all people in a list.

PUT
/lists/{listId}/people/{personId}

Add a person to a list.

DELETE
/lists/{listId}/people/{personId}

Remove a person from a list.

GET
/v2/lists/{id}/people

Fetches all people in a list.

PUT
/v2/lists/{listId}/people/{personId}

Add a person to a list.

DELETE
/v2/lists/{listId}/people/{personId}

Remove a person from a list.

### People (Import Emails)

POST
/people/{id}/import-email

Imports people email.

### People (Status tags)

POST
/people/tags

Adds tags to people.

DELETE
/people/tags

Removes tags from people.

### Projects

POST
/opportunities/{id}/completion

Adds a completion percentage to an opportunity

GET
/projects

Fetches all projects.

POST
/projects

Creates a project

GET
/projects/{id}

Fetches a project by ID

PUT
/projects/{id}

Updates a project

DELETE
/projects/{id}

Deletes a project by ID

GET
/v3/projects

Fetches all projects.

POST
/v3/projects

Creates a project

GET
/v3/projects/{id}

Fetches a project by ID

PUT
/v3/projects/{id}

Updates a project

DELETE
/v3/projects/{id}

Archive or delete a project

GET
/v3/projects/{id}/actions

Fetches all Actions from a particular Project.

PUT
/v3/projects/{id}/actions

Update Actions

PUT
/v3/projects/{id}/completion

Updates the completion percentage on a project

GET
/v3/projects/{id}/consultants

Fetches all consultants belonging to a project.

POST
/v3/projects/{id}/consultants

Adds a consultant to a project.

DELETE
/v3/projects/{id}/consultants/{userId}

Removes a consultant from a project

PUT
/v3/projects/{id}/convert

Convert a project from one type to another

GET
/v3/projects/{id}/office-groups

Fetches all office groups belonging to a project.

POST
/v3/projects/{id}/office-groups

Adds an office group to a project.

DELETE
/v3/projects/{id}/office-groups/{officeGroupId}

Removes an office group from a project

GET
/v3/projects/{id}/regions

Fetches all regions belonging to a project.

POST
/v3/projects/{id}/regions

Adds a region to a project.

DELETE
/v3/projects/{id}/regions/{regionId}

Removes a region from a project

### Projects (Candidates)

POST
/assignments/{id}/candidates/statuses

Adds pipeline tags to candidates.

DELETE
/assignments/{id}/candidates/statuses

Removes pipeline tags from candidates.

POST
/assignments/candidates

Adds a person as a candidate to an assignment.

GET
/projects/{id}/candidates

Fetches candidates from a specific assignment.

POST
/v2/assignments/candidates

Adds a person as a candidate to an assignment.

GET
/v2/projects/{id}/candidates

Fetches candidates from a specific project.

GET
/v3/projects/{id}/candidates

Fetches candidates from a specific project.

DELETE
/v3/projects/{id}/candidates

Removes a project candidate by ID.

POST
/v3/projects/{id}/candidates/statuses

Adds pipeline tags to candidates.

DELETE
/v3/projects/{id}/candidates/statuses

Removes pipeline tags from candidates.

POST
/v3/projects/candidates

Adds a person as a candidate to a project.

### Projects (Contacts)

GET
/v3/projects/{id}/contacts

Fetches contacts from a specific project.

POST
/v3/projects/{id}/contacts

Adds a person as a contact to a project.

DELETE
/v3/projects/{id}/contacts/{contactId}

Removes a person as a contact from a project.

### Billing

GET
/projects/{id}/billing

Fetches billing information for an item.

POST
/projects/{id}/billing/contact

Adds the contact to a project billing.

DELETE
/projects/{id}/billing/contact/{personId}

Removes the contact from project billing.

GET
/projects/{projectId}/billing/contact

Fetches the project billing contact

POST
/v2/projects/{id}/billing/contact

Adds the contact to a project billing.

DELETE
/v2/projects/{id}/billing/contact/{personId}

Removes the contact from project billing.

GET
/v2/projects/{projectId}/billing/contact

Fetches the project billing contact

GET
/v3/projects/{project}/billing

Fetches billing information for an item.

### Billing (Invoices)

GET
/invoice-templates

Fetches all the invoice templates.

GET
/invoices

Fetches all invoices.

GET
/invoices/{id}

Fetches a invoice by ID.

DELETE
/invoices/{invoiceId}

Deletes an invoice by ID.

PUT
/invoices/{invoiceId}/lock

Locks an invoice.

PUT
/invoices/{invoiceId}/unlock

Unlocks an invoice.

POST
/projects/{id}/invoices

Adds invoice to billing.

PUT
/projects/{id}/invoices/{invoiceId}

Updates an invoice.

GET
/v3/invoices

Fetches all invoices.

GET
/v3/invoices/{invoice}

Fetches a invoice by ID.

DELETE
/v3/invoices/{invoice}

Deletes an invoice by ID.

PUT
/v3/invoices/{invoice}/lock

Locks an invoice.

PUT
/v3/invoices/{invoice}/unlock

Unlocks an invoice.

POST
/v3/projects/{project}/invoices

Adds invoice to billing.

PUT
/v3/projects/{project}/invoices/{invoice}

Updates an invoice.

### Billing (Revenues)

POST
/projects/{projectId}/revenues

Creates a revenue.

PUT
/projects/{projectId}/revenues/{revenueId}

Updates a revenue

GET
/revenues

Fetches all revenues.

GET
/revenues/{id}

Fetches a revenue by ID.

DELETE
/revenues/{revenueId}

Deletes revenue item.

PUT
/revenues/{revenueId}/lock

Locks a revenue.

PUT
/revenues/{revenueId}/unlock

Unlocks a revenue.

POST
/v3/projects/{project}/revenues

Creates a revenue.

PUT
/v3/projects/{project}/revenues/{revenue}

Updates a revenue

GET
/v3/revenues

Fetches all revenues.

GET
/v3/revenues/{revenue}

Fetches a revenue by ID.

DELETE
/v3/revenues/{revenue}

Deletes revenue item.

PUT
/v3/revenues/{revenue}/lock

Locks a revenue.

PUT
/v3/revenues/{revenue}/unlock

Unlocks a revenue.

### Billing (Fixed Fees)

GET
/fixed-fees

Fetches all fixed fees.

GET
/fixed-fees/{fixedFeeId}

Fetches a fixed fee by ID.

DELETE
/fixed-fees/{fixedFeeId}

Deletes fixed fee item.

PUT
/fixed-fees/{fixedFeeId}/lock

Locks a fixed fee.

PUT
/fixed-fees/{fixedFeeId}/unlock

Unlocks a fixed fee.

GET
/projects/{id}/fixed-fees

Fetches all fixed fees by project ID.

POST
/projects/{id}/fixed-fees

Adds new fixed fee to billing.

PUT
/projects/{id}/fixed-fees/{fixedFeeId}

Updates a fixed fee.

GET
/v3/fixed-fees

Fetches all fixed fees.

GET
/v3/fixed-fees/{fixedFee}

Fetches a fixed fee by ID.

DELETE
/v3/fixed-fees/{fixedFee}

Deletes fixed fee item.

PUT
/v3/fixed-fees/{fixedFee}/lock

Locks a fixed fee.

PUT
/v3/fixed-fees/{fixedFee}/unlock

Unlocks a fixed fee.

GET
/v3/projects/{project}/fixed-fees

Fetches all fixed fees by project ID.

POST
/v3/projects/{project}/fixed-fees

Adds new fixed fee to billing.

PUT
/v3/projects/{project}/fixed-fees/{fixedFee}

Updates a fixed fee.

### Billing (Percent Splits)

GET
/percent-splits

Fetches all percent splits.

### Companies

GET
/companies

Fetches all companies.

POST
/companies

Creates a company

GET
/companies/{id}

Fetches a company by ID

PUT
/companies/{id}

Updates a company

DELETE
/companies/{id}

Deletes a company by ID

GET
/v2/companies

Fetches all companies.

POST
/v2/companies

Creates a company

GET
/v2/companies/{id}

Fetches a company by ID

PUT
/v2/companies/{id}

Updates a company

DELETE
/v2/companies/{id}

Deletes a company by ID

GET
/v3/companies

Fetches all companies.

POST
/v3/companies

Creates a company

GET
/v3/companies/{id}

Fetches a company by ID

PUT
/v3/companies/{id}

Updates a company

DELETE
/v3/companies/{id}

Deletes a company by ID

GET
/v3/companies/{id}/consultants

Fetches all consultants belonging to a company.

POST
/v3/companies/{id}/consultants

Adds a consultant to a company.

DELETE
/v3/companies/{id}/consultants/{userId}

Removes a consultant from a company

GET
/v3/companies/{id}/office-groups

Fetches all office groups belonging to a company.

POST
/v3/companies/{id}/office-groups

Adds an office group to a company.

DELETE
/v3/companies/{id}/office-groups/{officeGroupId}

Removes an office group from a company

GET
/v3/companies/{id}/regions

Fetches all regions belonging to a company.

POST
/v3/companies/{id}/regions

Adds a region to a company.

DELETE
/v3/companies/{id}/regions/{regionId}

Removes a region from a company

### Companies (Links)

POST
/companies/{id}/links

Adds a new link to a company.

PUT
/companies/{id}/links/{linkId}

Updates a link on a company.

DELETE
/companies/{id}/links/{linkId}

Deletes a link on a company.

### Clients

GET
/clients

Fetches all clients.

GET
/v2/clients

Fetches all clients.

GET
/v3/clients

Fetches all clients.

### Lists

GET
/lists

Fetches all lists.

POST
/lists

Creates a list

GET
/lists/{id}

Fetches a list by ID

PUT
/lists/{id}

Updates a list

DELETE
/lists/{id}

Deletes a list by ID

GET
/lists/{id}/people

Fetches all people in a list.

PUT
/lists/{listId}/people/{personId}

Add a person to a list.

DELETE
/lists/{listId}/people/{personId}

Remove a person from a list.

GET
/v2/lists/{id}/people

Fetches all people in a list.

PUT
/v2/lists/{listId}/people/{personId}

Add a person to a list.

DELETE
/v2/lists/{listId}/people/{personId}

Remove a person from a list.

### Notes

GET
/{type}/{id}/notes

Retrieves all notes for an item.

POST
/{type}/{id}/notes

Adds notes to an item.

PUT
/{type}/{id}/notes/{noteId}

Updates a note on an item.

DELETE
/{type}/{id}/notes/{noteId}

Deletes a note from an item.

GET
/notes

Fetches all notes

POST
/people/notes

Adds notes to one or more people.

PUT
/people/notes/{id}

Updates a note.

DELETE
/people/notes/{id}

Deletes a note.

### Status tags

POST
/{type}/{id}/status/{statusId}

Adds or updates a status for an item.

POST
/people/tags

Adds tags to people.

DELETE
/people/tags

Removes tags from people.

GET
/statuses/{type}

Fetches all status tags of a particular type.

### Categories

GET
/categories

Fetches all status tags of a particular type.

GET
/v2/categories/{category}

Fetches category values of a particular type by id or search term.

### Custom Values

GET
/{type}/{id}/additional-info

Retrieves all custom values for an item.

PUT
/{type}/{id}/additional-info

Adds or updates a custom value for an item.

DELETE
/{type}/{id}/additional-info

Deletes a custom value from an item.

### Custom Fields

GET
/custom-fields/{type}/

Retrieves all custom fields of a particular type

GET
/custom-fields/{type}/{fieldId}

Retrieves a custom field by ID

### Search Firm Users

GET
/search-users

Fetches all users for the search firm

### Off-Limits

GET
/off-limits/agreements/{modelType}

Retrieves all off-limits agreements for people or companies

POST
/off-limits/agreements/{modelType}

Creates an off-limits agreement for a person or a company

PUT
/off-limits/agreements/{modelType}/{agreementId}

Updates an off-limits agreement for a person or a company

DELETE
/off-limits/agreements/{modelType}/{agreementId}

Deletes an off-limits agreement for a person or a company

GET
/off-limits/agreements/{type}/{id}

Retrieves all off-limits agreements for a specific person or a company

### Documents

POST
/{type}/{id}/documents

Add documents and attachments.

GET
/v2/{type}/{id}/documents/{documentId}

Download documents and attachments.

### Meetings

GET
/{type}/{id}/meetings

Retrieves all meetings for an item.

GET
/graph/connected

Fetches Microsoft Graph details on connected accounts.

GET
/meetings

Fetches all meetings.

POST
/meetings

Creates a meeting.

GET
/meetings/{id}

Fetches a meeting by ID.

PUT
/meetings/{id}

Updates a meeting.

DELETE
/meetings/{id}

Deletes a meeting.

PUT
/meetings/{id}/pinned

Updates a meeting's pinned status.

### Tasks

GET
/{type}/{id}/tasks

Retrieves all tasks for an item.

GET
/tasks

Fetches all tasks.

POST
/tasks

Creates a task.

GET
/tasks/{id}

Fetches a task by ID.

PUT
/tasks/{id}

Updates a task.

DELETE
/tasks/{id}

Deletes a task.

PUT
/tasks/{id}/done

Updates a task's completion status.

PUT
/tasks/{id}/pinned

Updates a task's pinned status.

PUT
/tasks/{id}/priority

Updates a task's priority.

GET
/v3/tasks

Fetches all tasks.

POST
/v3/tasks

Creates a task.

GET
/v3/tasks/{id}

Fetches a task by ID.

PUT
/v3/tasks/{id}

Updates a task.

DELETE
/v3/tasks/{id}

Deletes a task.

PUT
/v3/tasks/{id}/done

Updates a task's completion status.

PUT
/v3/tasks/{id}/pinned

Updates a task's pinned status.

PUT
/v3/tasks/{id}/priority

Updates a task's priority.

### Relationships

GET
/relationship-labels

Fetches relationship labels.

GET
/relationships

Fetches relationships for a particular type.

POST
/relationships

Creates a new relationship

PUT
/relationships/{id}

Updates a relationship

DELETE
/relationships/{id}

Deletes a relationship

#### Schemas

Bucket Stats Tags

Career

Company Link Types

Company Type

Person Link Types

Company Store Request Body

Company Update Request Body

Category

Person Aspirations Request Body

Person Confidential Request Body

Person Notes Store Response

Person Store Request Body

Person Update Request Body

Person Email Store Request Body

Person Phone Number Store Request Body

Candidates Tags Store Request Body

Candidates Tags Store Response

Person Tags Store Request Body

Person Tags Store Response

Candidates Store Request Body

Candidates Store Response

List People Update Response

Project Store Request Body

Project Update Request Body

Task Store Request Body

Company Store Request Body

Company Store Request Body

List People Update Response

Candidates Store Request Body

Candidates Store Response

Person Store Request Body

Person Update Request Body

Task Store Request Body

Company Store Request Body

Company Store Request Body

Project Contacts Store Request Body

Person Store Request Body

Person Update Request Body

Candidates Tags Store Request Body

Candidates Tags Store Response

Candidates Store Request Body

Candidates Store Response

Project Store Request Body

Project Store Request Body

Fixed Fee Store Request Body

Invoice Store Request Body

Invoice Lock Request Body

Revenue Store Request Body

Custom Value Update Request Body

Document Request Body

Person Email Request Body

List Store Request Body

Off-limit Agreement Request Body

Person Education Request Body

Person Position Request Body

Person multiple Positions Request Body

Person Current Status Request Body

Meeting Request Body

Meeting Channels Request Body

Meeting Owners Request Body

Meeting Update Pinned

Person Update Request Body

Task Store

Task Update

Task Update Done

Task Update Priority

Task Update Pinned

Task Request Body

Task Channels Request Body

Opportunity Completion Request Body

Fixed Fee Store Request Body

Invoice Store Request Body

Revenue Store Request Body

Adding a Consultant Request Body

Adding an Office Group Request Body

Adding a Region Request Body

People store projects

Project Completion Request Body

Project Action Update Request Body

Person Link Request Body

Company Link Request Body

Project Store Delete Request Body

Project Update Request Body

List Pipeline

List

List Fields

List Manager Items

Lists Relationships

List Meta Items

Aspiration

Aspiration Interim

Aspiration NED

Aspiration Permanent

Confidential Information

Confidential Information For Permanent Positions

Confidential Information For NED Positions

Confidential Information For Interim Positions

Current Status

Person Document

Person Education

Person Language

Person Object

Person Position

Company

Company Manager Items

Company Meta Items

Company Permissions

Company Counts

Company Fields

Address

Email

Link

Phone

Custom Value

Custom Field

Document

Assignment Info

Person Default

Person NAL

Person Full

Person

Person Counts

Person Fields

Person Fields

Person Full

Person Profile

Person Relationships

Person Bucket Relationship

Person Billing Relationship

Person Project Relationship

Person Manager Items

Person Meta Info

Person Meta Info In Assignment Context

Person Completion Info

Person Candidate Info

Person Permissions

Person Meta Info

Person Counts NAL

Person Counts

Import Email Object

Import Email Relationships

Import Email Manager

Meeting Object

Meeting Fields

Notes Collection

Note

Off Limit Agreement

Project

Project Counts

Project Fields

Simple Company

Project Manager Items

Project Meta Items

Simple Meeting Object

Simple Note

Simple Status Object

Simple Task Object

Task Object

Task Fields

Task Pipeline

Office Group

Assignee

Calendarable Object

Microsoft Graph Object

Region

Billing Object

Billing Fee Split Object

Invoice Item Object

Billing Invoice Object

Invoice Full

Invoice Relationships

Invoice Counts

Invoice Fields

Invoice Template Object

Billing Recipient Object

Billing Recipient Relationships

Billing Revenue Object

Revenue Relationships

Revenue Fields

Researcher

Search User Relationships

Status Tag

Person Object

Person Position

Current Status

Company

Company Manager Items

Company Meta Items

Company Permissions

Company Counts

Company Fields

Assignment Info

Person Default

Person NAL

Person Full

Person

Person Counts

Person Fields

Person Fields

Person Full

Person Profile

Person Relationships

Person Bucket Relationship

Person Billing Relationship

Person Project Relationship

Person Manager Items

Person Meta Info

Person Meta Info In Assignment Context

Person Completion Info

Person Candidate Info

Person Permissions

Person Meta Info

Person Counts NAL

Person Counts

Due Diligence Check

Due Diligence Flag

Due Diligence History

Person Object

Person Position

Current Status

Company

Company Manager Items

Company Meta Items

Company Permissions

Company Counts

Company Fields

Person Default

Person NAL

Person Full

Person

Person Counts

Person Fields

Person Fields

Person Full

Person Profile

Person Relationships

Person Billing Relationship

Person Manager Items

Person Meta Info

Person Meta Info In Assignment Context

Person Completion Info

Person Candidate Info

Person Permissions

Person Meta Info

Person Counts NAL

Person Counts

Due Diligence Check

Due Diligence Flag

Due Diligence History

Project Action Tags

Project Info

Project Info

Project Info

Project

Project Counts

Project Fields

Simple Company

Project Manager Items

Project Meta Items

Task Object

Task Fields

Task Action

Office Group

Office Group User

Region

Region User

Billing Object

Billing Fixed Fee Object

Billing Invoice Object

Invoice Full

Invoice Relationships

Invoice Counts

Invoice Fields

Billing Revenue Object

Revenue Relationships

Revenue Fields

Search Firm User Object

Search Firm User Relationships

Search Firm User Projects

Search Firm User Companies

Search Firm User People

Search Firm User Invoices

Search Firm User Revenues

Search Firm User Delegates

Search Firm User Fields

Relationship Object

Relationship Object

Relationship Object

Relationship projects

Relationship companies

Relationship people

Relationship Label

Inverse Relationship Label

Due Diligence Phrase

Industry

Location

Invalid Data Response

Supported Currencies

Currency Amount

Person Store with Resume Body

NED Classification

Basic Item Info

Links

Pagination meta data

Custom Field Value

Off Limit Agreement Constraint

Access Level

Task Recursion

Recursion Type

Custom Value Request Object

Custom Value Request Object

Categories

Aspiration Status Value

Aspiration Status Text

Email Labels

Phone Labels

Team Size

Team Size ID

Position Type

