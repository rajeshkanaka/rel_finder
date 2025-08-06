# Ezekia API Documentation Analysis

## Base URL
https://ezekia.com/api

## Authentication
- Requires authorization (API Key provided)
- API Key: "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiOGM4ZGM4N2JhNGM2NWNkM2RmMWY3NTY0ZmU3OTRkNDdlZTEyMDkzNDdlYjEyNjVlMmI3N2QwNzkzNzY4MmMxN2NiZGZkZGIxZTU0NjVmNDciLCJpYXQiOjE3NTM5NDI4MTMuNjIxNTMzLCJuYmYiOjE3NTM5NDI4MTMuNjIxNTM3LCJleHAiOjE3NTY1MzQ4MTMuNjEyNTY3LCJzdWIiOiIxOTc1ODgzIiwic2NvcGVzIjpbXX0.1-ZqgbGCpjEmrCii_O4SK-UsdmXvkcSTrwXUzLxpvrbXnbSWBVTsmeP5k4i6LRpEQJ4kgXCf8C7GpYfIJAJFs8-W8HIBRze11u42LiDA0EBn7PasH8ZGTEc4RzEyl7aDMblwGYQxO-uNDmbEMV4LaDiwHScdR2r084903FjxoA8omcevSRUqk26EpR45lE--tYkyjtHfHCbhAw7daXXzDf4xm0MWWhJXsP8dV_dwhHZKH5YzK2kpVOdxi9L98zyDT-6PazpjaWioe6u65yPssiJ9E2Lvm7P_sRgUGurCvqjB5JUFIefJte9JCn1lPOPPJRmpRBfZFAI0zniS3sVdjAXOR14pqW2VOfk4nqOjg8TazY0_mzNLWozFpzSm3G9c41s7PK2P8TrDCvsuGDNuL34RIuOgqxVX8SKHZD8Ef5VrP3KmeC2XBVoxSjX6zHNWtjlbAh5lg3Gcwe8P3CCuJdr3MS2-sA570umzGxUT7OJ-A76kulXHD4xTczYOb2_PwwaEr7jernx6HuTzhXjLtLuamhDo-JWNtyHQL47h2jyv41hjTvu3jbeV10Qs2_capc-qLDrSmhWHAEjSu-kAFKehw1X16uBIkdj5fdxmUZ6ayLUvx-hz1QuymowRpzbUHYErpYKj80Y1_uARvBDqMxMDbSfBFBQl1LrDqtQbqtw"

## Discovered Endpoints

### People (Profile)
- GET /people - Fetches all people
- POST /people - Creates a person
- GET /people/{id} - Fetches a person by ID
- PUT /people/{id} - Updates a person
- DELETE /people/{id} - Deletes a person by ID
- GET /v2/people - Fetches all people (v2)
- POST /v2/people - Creates a person (v2)
- GET /v2/people/{id} - Fetches a person by ID (v2)

### Search Firm Users
- GET /search-users - Fetches all users for the search firm

### Companies
- GET /companies - Fetches all companies
- POST /companies - Creates a company
- GET /companies/{id} - Fetches a company by ID
- PUT /companies/{id} - Updates a company
- DELETE /companies/{id} - Deletes a company by ID
- GET /v2/companies - Fetches all companies (v2)
- POST /v2/companies - Creates a company (v2)
- GET /v2/companies/{id} - Fetches a company by ID (v2)
- PUT /v2/companies/{id} - Updates a company (v2)
- DELETE /v2/companies/{id} - Deletes a company by ID (v2)
- GET /v3/companies - Fetches all companies (v3)
- POST /v3/companies - Creates a company (v3)
- GET /v3/companies/{id} - Fetches a company by ID (v3)
- PUT /v3/companies/{id} - Updates a company (v3)
- DELETE /v3/companies/{id} - Deletes a company by ID (v3)

### Companies (Links)
- POST /companies/{id}/links - Adds a new link to a company
- PUT /companies/{id}/links/{linkId} - Updates a link on a company
- DELETE /companies/{id}/links/{linkId} - Deletes a link on a company

## Need to Explore
- Projects endpoints
- Assignments endpoints
- Placements endpoints
- Other relationship endpoints


### People (Additional Details)
- GET /v2/people/{personId}/positions - Gets all positions for a person (v2)
- POST /v2/people/{personId}/positions - Creates a position for a person (v2)
- PUT /v2/people/{personId}/positions/{positionId} - Updates a position for a person (v2)
- DELETE /v2/people/{personId}/positions/{positionId} - Deletes a position for a person (v2)

### People (Confidential Details)
- POST /people/{personId}/confidential - Sets confidential details for a person

### People (Aspirations)
- POST /people/{personId}/aspirations - Sets aspiration details for a person

### People (Current Status)
- POST /people/{personId}/current-status - Sets current status for a person

### People (Emails)
- POST /people/{id}/emails - Adds a new email address to a person
- PUT /people/{id}/emails/{emailId} - Updates an email address on a person
- DELETE /people/{id}/emails/{emailId} - Deletes an email address from a person

### People (Phones)
- POST /people/{id}/phones - Adds a new phone number to a person
- PUT /people/{id}/phones/{phoneId} - Updates a phone number on a person
- DELETE /people/{id}/phones/{phoneId} - Deletes a phone number from a person

### People (Links)
- POST /people/{id}/links - Adds a new link to a person
- PUT /people/{id}/links/{linkId} - Updates a link on a person
- DELETE /people/{id}/links/{linkId} - Deletes a link on a person

### People (Positions)
- GET /people/{personId}/positions - Gets all positions for a person
- POST /people/{personId}/positions - Creates a position for a person
- PUT /people/{personId}/positions/{positionId} - Updates a position for a person
- DELETE /people/{personId}/positions/{positionId} - Deletes a position for a person

### People (Education/Qualifications)
- GET /people/{personId}/education - Gets all educations for a person
- POST /people/{personId}/education - Creates an education for a person
- PUT /people/{personId}/education/{educationId} - Updates an education for a person
- DELETE /people/{personId}/education/{educationId} - Deletes an education for a person

### People (Notes)
- POST /people/notes - Adds notes to one or more people
- PUT /people/notes/{id} - Updates a note
- DELETE /people/notes/{id} - Deletes a note

### People (Lists)
- GET /lists/{id}/people - Fetches all people in a list


### Projects
- GET /projects - Fetches all projects
- POST /projects - Creates a project
- GET /projects/{id} - Fetches a project by ID
- PUT /projects/{id} - Updates a project
- DELETE /projects/{id} - Deletes a project by ID
- GET /v3/projects - Fetches all projects (v3)
- POST /v3/projects - Creates a project (v3)
- GET /v3/projects/{id} - Fetches a project by ID (v3)
- PUT /v3/projects/{id} - Updates a project (v3)
- DELETE /v3/projects/{id} - Archive or delete a project (v3)

### Projects (Advanced v3)
- GET /v3/projects/{id}/actions - Fetches all Actions from a particular Project
- PUT /v3/projects/{id}/actions - Update Actions
- PUT /v3/projects/{id}/completion - Updates the completion percentage on a project
- GET /v3/projects/{id}/consultants - Fetches all consultants belonging to a project
- POST /v3/projects/{id}/consultants - Adds a consultant to a project
- DELETE /v3/projects/{id}/consultants/{userId} - Removes a consultant from a project
- PUT /v3/projects/{id}/convert - Convert a project from one type to another
- GET /v3/projects/{id}/office-groups - Fetches all office groups belonging to a project
- POST /v3/projects/{id}/office-groups - Adds an office group to a project
- DELETE /v3/projects/{id}/office-groups/{officeGroupId} - Removes an office group from a project
- GET /v3/projects/{id}/regions - Fetches all regions belonging to a project
- POST /v3/projects/{id}/regions - Adds a region to a project
- DELETE /v3/projects/{id}/regions/{regionId} - Removes a region from a project

### Projects (Candidates)
- POST /assignments/{id}/candidates/statuses - Adds pipeline tags to candidates
- DELETE /assignments/{id}/candidates/statuses - Removes pipeline tags from candidates
- POST /assignments/candidates - Adds a person as a candidate to an assignment
- GET /projects/{id}/candidates - Fetches candidates from a specific assignment
- POST /v2/assignments/candidates - Adds a person as a candidate to an assignment (v2)
- GET /v2/projects/{id}/candidates - Fetches candidates from a specific project (v2)
- GET /v3/projects/{id}/candidates - Fetches candidates from a specific project (v3)
- DELETE /v3/projects/{id}/candidates - Removes a project candidate by ID


### Additional Endpoints Found

### Projects (Contacts)
- GET /v3/projects/{id}/contacts - Fetches contacts from a specific project
- POST /v3/projects/{id}/contacts - Adds a person as a contact to a project
- DELETE /v3/projects/{id}/contacts/{contactId} - Removes a person as a contact from a project

### Billing
- GET /projects/{id}/billing - Fetches billing information for an item
- POST /projects/{id}/billing/contact - Adds the contact to a project billing
- DELETE /projects/{id}/billing/contact/{personId} - Removes the contact from project billing
- GET /projects/{projectId}/billing/contact - Fetches the project billing contact

### Billing (Invoices)
- GET /invoice-templates - Fetches all the invoice templates
- GET /invoices - Fetches all invoices
- GET /invoices/{id} - Fetches a invoice by ID
- DELETE /invoices/{invoiceId} - Deletes an invoice by ID
- PUT /invoices/{invoiceId}/lock - Locks an invoice
- PUT /invoices/{invoiceId}/unlock - Unlocks an invoice
- POST /projects/{id}/invoices - Adds invoice to billing
- PUT /projects/{id}/invoices/{invoiceId} - Updates an invoice

### Billing (Revenues)
- POST /projects/{projectId}/revenues - Creates a revenue
- PUT /projects/{projectId}/revenues/{revenueId} - Updates a revenue
- GET /revenues - Fetches all revenues
- GET /revenues/{id} - Fetches a revenue by ID
- DELETE /revenues/{revenueId} - Deletes revenue item
- PUT /revenues/{revenueId}/lock - Locks a revenue
- PUT /revenues/{revenueId}/unlock - Unlocks a revenue

### Billing (Fixed Fees)
- GET /fixed-fees - Fetches all fixed fees
- GET /fixed-fees/{fixedFeeId} - Fetches a fixed fee by ID
- DELETE /fixed-fees/{fixedFeeId} - Deletes fixed fee item
- PUT /fixed-fees/{fixedFeeId}/lock - Locks a fixed fee
- PUT /fixed-fees/{fixedFeeId}/unlock - Unlocks a fixed fee
- GET /projects/{id}/fixed-fees - Fetches all fixed fees by project ID
- POST /projects/{id}/fixed-fees - Adds new fixed fee to billing
- PUT /projects/{id}/fixed-fees/{fixedFeeId} - Updates a fixed fee

### Billing (Percent Splits)
- GET /percent-splits - Fetches all percent splits

### Clients
- GET /clients - Fetches all clients
- GET /v2/clients - Fetches all clients (v2)
- GET /v3/clients - Fetches all clients (v3)

### Lists
- GET /lists - Fetches all lists
- POST /lists - Creates a list
- GET /lists/{id} - Fetches a list by ID
- PUT /lists/{id} - Updates a list
- DELETE /lists/{id} - Deletes a list by ID
- GET /lists/{id}/people - Fetches all people in a list
- PUT /lists/{listId}/people/{personId} - Add a person to a list
- DELETE /lists/{listId}/people/{personId} - Remove a person from a list

### Notes
- GET /{type}/{id}/notes - Retrieves all notes for an item
- POST /{type}/{id}/notes - Adds notes to an item
- PUT /{type}/{id}/notes/{noteId} - Updates a note on an item
- DELETE /{type}/{id}/notes/{noteId} - Deletes a note from an item
- GET /notes - Fetches all notes

### Status tags
- POST /{type}/{id}/status/{statusId} - Adds or updates a status for an item
- POST /people/tags - Adds tags to people
- DELETE /people/tags - Removes tags from people
- GET /statuses/{type} - Fetches all status tags of a particular type

### Categories
- GET /categories - Fetches all status tags of a particular type
- GET /v2/categories/{category} - Fetches category values of a particular type by id or search term

### Custom Values
- GET /{type}/{id}/additional-info - Retrieves all custom values for an item
- PUT /{type}/{id}/additional-info - Adds or updates a custom value for an item
- DELETE /{type}/{id}/additional-info - Deletes a custom value from an item

### Custom Fields
- GET /custom-fields/{type}/ - Retrieves all custom fields of a particular type
- GET /custom-fields/{type}/{fieldId} - Retrieves a custom field by ID

### Search Firm Users
- GET /search-users - Fetches all users for the search firm

### Off-Limits
- GET /off-limits/agreements/{modelType} - Retrieves all off-limits agreements for people or companies
- POST /off-limits/agreements/{modelType} - Creates an off-limits agreement for a person or a company
- PUT /off-limits/agreements/{modelType}/{agreementId} - Updates an off-limits agreement for a person or a company
- DELETE /off-limits/agreements/{modelType}/{agreementId} - Deletes an off-limits agreement for a person or a company
- GET /off-limits/agreements/{type}/{id} - Retrieves all off-limits agreements for a specific person or a company

### Documents
- POST /{type}/{id}/documents - Add documents and attachments
- GET /v2/{type}/{id}/documents/{documentId} - Download documents and attachments

### Meetings
- GET /{type}/{id}/meetings - Retrieves all meetings for an item
- GET /graph/connected - Fetches Microsoft Graph details on connected accounts
- GET /meetings - Fetches all meetings
- POST /meetings - Creates a meeting
- GET /meetings/{id} - Fetches a meeting by ID
- PUT /meetings/{id} - Updates a meeting
- DELETE /meetings/{id} - Deletes a meeting
- PUT /meetings/{id}/pinned - Updates a meeting's pinned status

### Tasks
- GET /{type}/{id}/tasks - Retrieves all tasks for an item
- GET /tasks - Fetches all tasks
- POST /tasks - Creates a task
- GET /tasks/{id} - Fetches a task by ID
- PUT /tasks/{id} - Updates a task
- DELETE /tasks/{id} - Deletes a task
- PUT /tasks/{id}/done - Updates a task's completion status
- PUT /tasks/{id}/pinned - Updates a task's pinned status
- PUT /tasks/{id}/priority - Updates a task's priority

### Relationships
- GET /relationship-labels - Fetches relationship labels
- GET /relationships - Fetches relationships for a particular type
- POST /relationships - Creates a new relationship
- PUT /relationships/{id} - Updates a relationship
- DELETE /relationships/{id} - Deletes a relationship

