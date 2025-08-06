#!/usr/bin/env python3
"""
Ezekia API Company Relationship Finder (Optimized)

This script searches for all possible relationships and records for a given company name
across the Ezekia API endpoints using only the latest/best API version for each endpoint.

Usage:
    python company_relationship_finder_optimized.py "Company Name"

Author: AI Assistant
Date: 2025-08-06
"""

import requests
import json
import sys
from typing import Dict, List, Any, Optional
from urllib.parse import quote
import time

class EzekiaCompanyFinderOptimized:
    def __init__(self, api_key: str, base_url: str = "https://ezekia.com/api"):
        """
        Initialize the Ezekia API client
        
        Args:
            api_key: JWT token for API authentication
            base_url: Base URL for the Ezekia API
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.results = {}
        
        # Define the best API version for each endpoint
        self.api_endpoints = {
            'companies': '/v3/companies',           # Use latest v3
            'projects': '/v3/projects',             # Use latest v3
            'people': '/v3/people',                 # Use latest v3
            'lists': '/lists',                      # Only one version
            'invoices': '/v3/invoices',             # Use latest v3
            'notes': '/notes',                      # Only one version
            'tasks': '/v3/tasks',                   # Use latest v3
            'meetings': '/meetings',                # Only one version
            'candidates': '/v3/projects/{}/candidates',  # Use latest v3
            'relationships': '/relationships'        # Only one version (but needs params)
        }
        
    def make_request(self, endpoint: str, method: str = 'GET', params: Dict = None, data: Dict = None) -> Optional[Dict]:
        """
        Make a request to the Ezekia API
        
        Args:
            endpoint: API endpoint (without base URL)
            method: HTTP method (GET, POST, etc.)
            params: Query parameters
            data: Request body data
            
        Returns:
            Response data as dictionary or None if error
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                params=params,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return None
            else:
                print(f"API Error {response.status_code} for {endpoint}: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Request error for {endpoint}: {str(e)}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON decode error for {endpoint}: {str(e)}")
            return None
    
    def search_companies(self, company_name: str) -> List[Dict]:
        """
        Search for companies by name using the latest API version
        
        Args:
            company_name: Name of the company to search for
            
        Returns:
            List of matching companies
        """
        companies = []
        endpoint = self.api_endpoints['companies']
        
        print(f"Searching companies in {endpoint}...")
        data = self.make_request(endpoint)
        
        if data and isinstance(data, (list, dict)):
            # Handle different response formats
            company_list = data if isinstance(data, list) else data.get('data', [])
            
            for company in company_list:
                if isinstance(company, dict):
                    company_display_name = company.get('name', '').lower()
                    if company_name.lower() in company_display_name:
                        company['api_version'] = endpoint
                        companies.append(company)
        
        return companies
    
    def get_company_details(self, company_id: str) -> Optional[Dict]:
        """
        Get detailed information about a specific company
        
        Args:
            company_id: ID of the company
            
        Returns:
            Company details or None
        """
        endpoint = f"{self.api_endpoints['companies']}/{company_id}"
        return self.make_request(endpoint)
    
    def find_projects_by_company(self, company_name: str, company_id: str = None) -> List[Dict]:
        """
        Find projects associated with the company
        
        Args:
            company_name: Name of the company
            company_id: ID of the company (if known)
            
        Returns:
            List of associated projects
        """
        projects = []
        endpoint = self.api_endpoints['projects']
        
        print(f"Searching projects in {endpoint}...")
        data = self.make_request(endpoint)
        
        if data and isinstance(data, (list, dict)):
            project_list = data if isinstance(data, list) else data.get('data', [])
            
            for project in project_list:
                if isinstance(project, dict):
                    # Check if company name appears in project details
                    project_str = json.dumps(project).lower()
                    if company_name.lower() in project_str:
                        project['found_in'] = endpoint
                        projects.append(project)
        
        return projects
    
    def find_people_by_company(self, company_name: str) -> List[Dict]:
        """
        Find people associated with the company
        
        Args:
            company_name: Name of the company
            
        Returns:
            List of associated people
        """
        people = []
        endpoint = self.api_endpoints['people']
        
        print(f"Searching people in {endpoint}...")
        data = self.make_request(endpoint)
        
        if data and isinstance(data, (list, dict)):
            people_list = data if isinstance(data, list) else data.get('data', [])
            
            for person in people_list:
                if isinstance(person, dict):
                    # Check if company name appears in person details
                    person_str = json.dumps(person).lower()
                    if company_name.lower() in person_str:
                        person['found_in'] = endpoint
                        people.append(person)
        
        return people
    
    def find_lists_by_company(self, company_name: str) -> List[Dict]:
        """
        Find lists that contain the company name
        
        Args:
            company_name: Name of the company
            
        Returns:
            List of associated lists
        """
        lists = []
        endpoint = self.api_endpoints['lists']
        
        print(f"Searching lists in {endpoint}...")
        data = self.make_request(endpoint)
        
        if data and isinstance(data, (list, dict)):
            lists_data = data if isinstance(data, list) else data.get('data', [])
            
            for list_item in lists_data:
                if isinstance(list_item, dict):
                    # Check if company name appears in list details
                    list_str = json.dumps(list_item).lower()
                    if company_name.lower() in list_str:
                        lists.append(list_item)
        
        return lists
    
    def find_relationships_by_company(self, company_name: str, company_ids: List[str] = None) -> List[Dict]:
        """
        Find relationships involving the company
        Note: The relationships endpoint requires specific parameters, so we'll skip it
        or implement it properly if we have the required parameters
        
        Args:
            company_name: Name of the company
            company_ids: List of company IDs to search relationships for
            
        Returns:
            List of relationships
        """
        relationships = []
        
        # Skip relationships endpoint as it requires specific parameters
        # that we don't have (id, type, relatedType)
        print("Skipping relationships (requires specific parameters)...")
        
        return relationships
    
    def find_candidates_by_company(self, company_name: str, project_ids: List[str] = None) -> List[Dict]:
        """
        Find candidates associated with company projects
        
        Args:
            company_name: Name of the company
            project_ids: List of project IDs to search in
            
        Returns:
            List of candidates
        """
        candidates = []
        
        # If we have specific project IDs, search within those projects
        if project_ids:
            # Remove duplicates from project_ids
            unique_project_ids = list(set(project_ids))
            
            for project_id in unique_project_ids:
                endpoint = self.api_endpoints['candidates'].format(project_id)
                
                print(f"Searching candidates in {endpoint}...")
                data = self.make_request(endpoint)
                
                if data and isinstance(data, (list, dict)):
                    candidates_data = data if isinstance(data, list) else data.get('data', [])
                    
                    for candidate in candidates_data:
                        if isinstance(candidate, dict):
                            candidate['project_id'] = project_id
                            candidate['found_in'] = endpoint
                            candidates.append(candidate)
                
                time.sleep(0.1)
        
        return candidates
    
    def find_invoices_by_company(self, company_name: str, project_ids: List[str] = None) -> List[Dict]:
        """
        Find invoices associated with the company
        
        Args:
            company_name: Name of the company
            project_ids: List of project IDs to search in
            
        Returns:
            List of invoices
        """
        invoices = []
        endpoint = self.api_endpoints['invoices']
        
        print(f"Searching invoices in {endpoint}...")
        data = self.make_request(endpoint)
        
        if data and isinstance(data, (list, dict)):
            invoices_data = data if isinstance(data, list) else data.get('data', [])
            
            for invoice in invoices_data:
                if isinstance(invoice, dict):
                    invoice_str = json.dumps(invoice).lower()
                    if company_name.lower() in invoice_str:
                        invoice['found_in'] = endpoint
                        invoices.append(invoice)
        
        return invoices
    
    def find_notes_by_company(self, company_name: str) -> List[Dict]:
        """
        Find notes mentioning the company
        
        Args:
            company_name: Name of the company
            
        Returns:
            List of notes
        """
        notes = []
        endpoint = self.api_endpoints['notes']
        
        print(f"Searching notes in {endpoint}...")
        data = self.make_request(endpoint)
        
        if data and isinstance(data, (list, dict)):
            notes_data = data if isinstance(data, list) else data.get('data', [])
            
            for note in notes_data:
                if isinstance(note, dict):
                    note_str = json.dumps(note).lower()
                    if company_name.lower() in note_str:
                        notes.append(note)
        
        return notes
    
    def find_tasks_by_company(self, company_name: str) -> List[Dict]:
        """
        Find tasks related to the company
        
        Args:
            company_name: Name of the company
            
        Returns:
            List of tasks
        """
        tasks = []
        endpoint = self.api_endpoints['tasks']
        
        print(f"Searching tasks in {endpoint}...")
        data = self.make_request(endpoint)
        
        if data and isinstance(data, (list, dict)):
            tasks_data = data if isinstance(data, list) else data.get('data', [])
            
            for task in tasks_data:
                if isinstance(task, dict):
                    task_str = json.dumps(task).lower()
                    if company_name.lower() in task_str:
                        task['found_in'] = endpoint
                        tasks.append(task)
        
        return tasks
    
    def find_meetings_by_company(self, company_name: str) -> List[Dict]:
        """
        Find meetings related to the company
        
        Args:
            company_name: Name of the company
            
        Returns:
            List of meetings
        """
        meetings = []
        endpoint = self.api_endpoints['meetings']
        
        print(f"Searching meetings in {endpoint}...")
        data = self.make_request(endpoint)
        
        if data and isinstance(data, (list, dict)):
            meetings_data = data if isinstance(data, list) else data.get('data', [])
            
            for meeting in meetings_data:
                if isinstance(meeting, dict):
                    meeting_str = json.dumps(meeting).lower()
                    if company_name.lower() in meeting_str:
                        meetings.append(meeting)
        
        return meetings
    
    def find_all_relationships(self, company_name: str) -> Dict[str, Any]:
        """
        Find all possible relationships and records for a company
        
        Args:
            company_name: Name of the company to search for
            
        Returns:
            Dictionary containing all found relationships
        """
        print(f"\\n🔍 Searching for all relationships for company: '{company_name}'")
        print("=" * 60)
        
        results = {
            'search_query': company_name,
            'companies': [],
            'projects': [],
            'people': [],
            'lists': [],
            'relationships': [],
            'candidates': [],
            'invoices': [],
            'notes': [],
            'tasks': [],
            'meetings': [],
            'summary': {}
        }
        
        # 1. Find matching companies
        print("\\n1. Searching for matching companies...")
        results['companies'] = self.search_companies(company_name)
        print(f"   Found {len(results['companies'])} matching companies")
        
        # 2. Find projects
        print("\\n2. Searching for related projects...")
        results['projects'] = self.find_projects_by_company(company_name)
        print(f"   Found {len(results['projects'])} related projects")
        
        # Extract unique project IDs for further searches
        project_ids = list(set([str(p.get('id', '')) for p in results['projects'] if p.get('id')]))
        
        # 3. Find people
        print("\\n3. Searching for related people...")
        results['people'] = self.find_people_by_company(company_name)
        print(f"   Found {len(results['people'])} related people")
        
        # 4. Find lists
        print("\\n4. Searching for related lists...")
        results['lists'] = self.find_lists_by_company(company_name)
        print(f"   Found {len(results['lists'])} related lists")
        
        # 5. Find relationships (skipped due to API requirements)
        print("\\n5. Searching for relationships...")
        company_ids = list(set([str(c.get('id', '')) for c in results['companies'] if c.get('id')]))
        results['relationships'] = self.find_relationships_by_company(company_name, company_ids)
        print(f"   Found {len(results['relationships'])} relationships")
        
        # 6. Find candidates
        print("\\n6. Searching for candidates...")
        results['candidates'] = self.find_candidates_by_company(company_name, project_ids)
        print(f"   Found {len(results['candidates'])} candidates")
        
        # 7. Find invoices
        print("\\n7. Searching for invoices...")
        results['invoices'] = self.find_invoices_by_company(company_name, project_ids)
        print(f"   Found {len(results['invoices'])} invoices")
        
        # 8. Find notes
        print("\\n8. Searching for notes...")
        results['notes'] = self.find_notes_by_company(company_name)
        print(f"   Found {len(results['notes'])} notes")
        
        # 9. Find tasks
        print("\\n9. Searching for tasks...")
        results['tasks'] = self.find_tasks_by_company(company_name)
        print(f"   Found {len(results['tasks'])} tasks")
        
        # 10. Find meetings
        print("\\n10. Searching for meetings...")
        results['meetings'] = self.find_meetings_by_company(company_name)
        print(f"    Found {len(results['meetings'])} meetings")
        
        # Generate summary
        results['summary'] = {
            'total_companies': len(results['companies']),
            'total_projects': len(results['projects']),
            'total_people': len(results['people']),
            'total_lists': len(results['lists']),
            'total_relationships': len(results['relationships']),
            'total_candidates': len(results['candidates']),
            'total_invoices': len(results['invoices']),
            'total_notes': len(results['notes']),
            'total_tasks': len(results['tasks']),
            'total_meetings': len(results['meetings']),
            'total_records': sum([
                len(results['companies']),
                len(results['projects']),
                len(results['people']),
                len(results['lists']),
                len(results['relationships']),
                len(results['candidates']),
                len(results['invoices']),
                len(results['notes']),
                len(results['tasks']),
                len(results['meetings'])
            ])
        }
        
        return results
    
    def print_summary(self, results: Dict[str, Any]):
        """
        Print a summary of the search results
        
        Args:
            results: Results dictionary from find_all_relationships
        """
        print("\\n" + "=" * 60)
        print(f"📊 SUMMARY FOR: {results['search_query']}")
        print("=" * 60)
        
        summary = results['summary']
        
        print(f"Companies found:     {summary['total_companies']}")
        print(f"Projects found:      {summary['total_projects']}")
        print(f"People found:        {summary['total_people']}")
        print(f"Lists found:         {summary['total_lists']}")
        print(f"Relationships found: {summary['total_relationships']}")
        print(f"Candidates found:    {summary['total_candidates']}")
        print(f"Invoices found:      {summary['total_invoices']}")
        print(f"Notes found:         {summary['total_notes']}")
        print(f"Tasks found:         {summary['total_tasks']}")
        print(f"Meetings found:      {summary['total_meetings']}")
        print("-" * 40)
        print(f"TOTAL RECORDS:       {summary['total_records']}")
        
        # Show some sample data if available (without duplicates)
        if results['companies']:
            print("\\n📋 Sample Companies:")
            unique_companies = {}
            for company in results['companies']:
                comp_id = company.get('id')
                if comp_id not in unique_companies:
                    unique_companies[comp_id] = company
            
            for i, company in enumerate(list(unique_companies.values())[:3], 1):
                print(f"   {i}. {company.get('name', 'N/A')} (ID: {company.get('id', 'N/A')})")
        
        if results['projects']:
            print("\\n📋 Sample Projects:")
            unique_projects = {}
            for project in results['projects']:
                proj_id = project.get('id')
                if proj_id not in unique_projects:
                    unique_projects[proj_id] = project
            
            for i, project in enumerate(list(unique_projects.values())[:3], 1):
                print(f"   {i}. {project.get('name', project.get('title', 'N/A'))} (ID: {project.get('id', 'N/A')})")
        
        if results['people']:
            print("\\n📋 Sample People:")
            for i, person in enumerate(results['people'][:3], 1):
                name = f"{person.get('first_name', '')} {person.get('last_name', '')}".strip()
                print(f"   {i}. {name or 'N/A'} (ID: {person.get('id', 'N/A')})")


def main():
    """
    Main function to run the company relationship finder
    """
    # API Configuration
    API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiOGM4ZGM4N2JhNGM2NWNkM2RmMWY3NTY0ZmU3OTRkNDdlZTEyMDkzNDdlYjEyNjVlMmI3N2QwNzkzNzY4MmMxN2NiZGZkZGIxZTU0NjVmNDciLCJpYXQiOjE3NTM5NDI4MTMuNjIxNTMzLCJuYmYiOjE3NTM5NDI4MTMuNjIxNTM3LCJleHAiOjE3NTY1MzQ4MTMuNjEyNTY3LCJzdWIiOiIxOTc1ODgzIiwic2NvcGVzIjpbXX0.1-ZqgbGCpjEmrCii_O4SK-UsdmXvkcSTrwXUzLxpvrbXnbSWBVTsmeP5k4i6LRpEQJ4kgXCf8C7GpYfIJAJFs8-W8HIBRze11u42LiDA0EBn7PasH8ZGTEc4RzEyl7aDMblwGYQxO-uNDmbEMV4LaDiwHScdR2r084903FjxoA8omcevSRUqk26EpR45lE--tYkyjtHfHCbhAw7daXXzDf4xm0MWWhJXsP8dV_dwhHZKH5YzK2kpVOdxi9L98zyDT-6PazpjaWioe6u65yPssiJ9E2Lvm7P_sRgUGurCvqjB5JUFIefJte9JCn1lPOPPJRmpRBfZFAI0zniS3sVdjAXOR14pqW2VOfk4nqOjg8TazY0_mzNLWozFpzSm3G9c41s7PK2P8TrDCvsuGDNuL34RIuOgqxVX8SKHZD8Ef5VrP3KmeC2XBVoxSjX6zHNWtjlbAh5lg3Gcwe8P3CCuJdr3MS2-sA570umzGxUT7OJ-A76kulXHD4xTczYOb2_PwwaEr7jernx6HuTzhXjLtLuamhDo-JWNtyHQL47h2jyv41hjTvu3jbeV10Qs2_capc-qLDrSmhWHAEjSu-kAFKehw1X16uBIkdj5fdxmUZ6ayLUvx-hz1QuymowRpzbUHYErpYKj80Y1_uARvBDqMxMDbSfBFBQl1LrDqtQbqtw"
    BASE_URL = "https://ezekia.com/api"
    
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python company_relationship_finder_optimized.py \"Company Name\"")
        print("\\nExamples:")
        print("  python company_relationship_finder_optimized.py \"Larsen & Toubro\"")
        print("  python company_relationship_finder_optimized.py \"Schneider Electric\"")
        print("  python company_relationship_finder_optimized.py \"Honeywell\"")
        sys.exit(1)
    
    company_name = sys.argv[1].strip()
    
    if not company_name:
        print("Error: Company name cannot be empty")
        sys.exit(1)
    
    # Initialize the finder
    finder = EzekiaCompanyFinderOptimized(API_KEY, BASE_URL)
    
    try:
        # Find all relationships
        results = finder.find_all_relationships(company_name)
        
        # Print summary
        finder.print_summary(results)
        
        # Save detailed results to JSON file
        output_filename = f"company_relationships_{company_name.replace(' ', '_').replace('&', 'and')}_optimized.json"
        
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"\\n💾 Detailed results saved to: {output_filename}")
        
        # Print some detailed information if records found
        if results['summary']['total_records'] > 0:
            print("\\n" + "=" * 60)
            print("📋 DETAILED BREAKDOWN")
            print("=" * 60)
            
            # Show unique company details
            if results['companies']:
                print("\\n🏢 COMPANIES:")
                unique_companies = {}
                for company in results['companies']:
                    comp_id = company.get('id')
                    if comp_id not in unique_companies:
                        unique_companies[comp_id] = company
                
                for i, company in enumerate(list(unique_companies.values()), 1):
                    print(f"  {i}. Name: {company.get('name', 'N/A')}")
                    print(f"     ID: {company.get('id', 'N/A')}")
                    print(f"     Type: {company.get('type', 'N/A')}")
                    print(f"     API Version: {company.get('api_version', 'N/A')}")
                    print()
            
            # Show unique project details
            if results['projects']:
                print("\\n📊 PROJECTS:")
                unique_projects = {}
                for project in results['projects']:
                    proj_id = project.get('id')
                    if proj_id not in unique_projects:
                        unique_projects[proj_id] = project
                
                for i, project in enumerate(list(unique_projects.values())[:5], 1):
                    print(f"  {i}. Name: {project.get('name', project.get('title', 'N/A'))}")
                    print(f"     ID: {project.get('id', 'N/A')}")
                    print(f"     Status: {project.get('status', 'N/A')}")
                    print(f"     Found in: {project.get('found_in', 'N/A')}")
                    print()
                
                if len(unique_projects) > 5:
                    print(f"     ... and {len(unique_projects) - 5} more projects")
            
            # Show people details
            if results['people']:
                print("\\n👥 PEOPLE:")
                for i, person in enumerate(results['people'][:5], 1):
                    name = f"{person.get('first_name', '')} {person.get('last_name', '')}".strip()
                    print(f"  {i}. Name: {name or 'N/A'}")
                    print(f"     ID: {person.get('id', 'N/A')}")
                    print(f"     Email: {person.get('email', 'N/A')}")
                    print(f"     Found in: {person.get('found_in', 'N/A')}")
                    print()
                
                if len(results['people']) > 5:
                    print(f"     ... and {len(results['people']) - 5} more people")
        
        else:
            print(f"\\n❌ No records found for company: '{company_name}'")
            print("\\nSuggestions:")
            print("- Check the spelling of the company name")
            print("- Try searching with partial company name")
            print("- Try different variations (with/without 'Ltd', 'Inc', etc.)")
    
    except KeyboardInterrupt:
        print("\\n\\n⚠️  Search interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\\n❌ An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

