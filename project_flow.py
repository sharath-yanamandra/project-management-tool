import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime, timedelta
import uuid

class DroneInspectionTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("InsightEye.AI - Drone Inspection Tracker")
        self.root.geometry("1200x750")
        self.root.configure(bg="#f5f5f5")
        
        self.data_file = "inspection_tasks.json"
        self.team_members = ["Project Manager", "Drone Pilot", "Data Engineer", "AI Specialist", "Report Analyst"]
        self.current_project = None
        
        # Load existing data or create new
        self.load_data()
        
        # Create UI
        self.create_ui()
        
    def load_data(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    self.data = json.load(file)
            else:
                self.data = {
                    "projects": [],
                    "workflow_template": self.create_workflow_template()
                }
                self.save_data()
        except Exception as e:
            messagebox.showerror("Data Load Error", f"Error loading data: {str(e)}")
            self.data = {
                "projects": [],
                "workflow_template": self.create_workflow_template()
            }
    
    def save_data(self):
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            messagebox.showerror("Data Save Error", f"Error saving data: {str(e)}")
    
    def create_workflow_template(self):
        # Create default workflow phases and tasks
        return [
            {
                "phase_id": "phase1",
                "phase_name": "Pre-Inspection Planning",
                "color": "#e1f5fe",
                "tasks": [
                    {"id": str(uuid.uuid4()), "name": "Inspection Schedule Planning", "assignee": "", "status": "Not Started", "notes": "", "duration": "4 hours"},
                    {"id": str(uuid.uuid4()), "name": "Weather & Radiation Forecasting", "assignee": "", "status": "Not Started", "notes": "", "duration": "2 hours"},
                    {"id": str(uuid.uuid4()), "name": "Flight Path & Mission Planning", "assignee": "", "status": "Not Started", "notes": "", "duration": "4 hours"},
                    {"id": str(uuid.uuid4()), "name": "Instruction Preparation for Drone Pilot", "assignee": "", "status": "Not Started", "notes": "", "duration": "2 hours"},
                    {"id": str(uuid.uuid4()), "name": "Equipment Check & Calibration", "assignee": "", "status": "Not Started", "notes": "", "duration": "3 hours"}
                ]
            },
            {
                "phase_id": "phase2",
                "phase_name": "Site Inspection",
                "color": "#e8f5e9",
                "tasks": [
                    {"id": str(uuid.uuid4()), "name": "Drone Pilot Briefing", "assignee": "", "status": "Not Started", "notes": "", "duration": "1 hour"},
                    {"id": str(uuid.uuid4()), "name": "Provide Flight Parameters & Requirements", "assignee": "", "status": "Not Started", "notes": "", "duration": "1 hour"},
                    {"id": str(uuid.uuid4()), "name": "Morning RGB Session: Soiling Detection", "assignee": "", "status": "Not Started", "notes": "", "duration": "3 hours"},
                    {"id": str(uuid.uuid4()), "name": "Midday Thermal Session: Hotspot Detection", "assignee": "", "status": "Not Started", "notes": "", "duration": "3 hours"},
                    {"id": str(uuid.uuid4()), "name": "Data Verification in Field", "assignee": "", "status": "Not Started", "notes": "", "duration": "2 hours"},
                    {"id": str(uuid.uuid4()), "name": "Immediate Quality Check", "assignee": "", "status": "Not Started", "notes": "", "duration": "2 hours"}
                ]
            },
            {
                "phase_id": "phase3",
                "phase_name": "Data Upload",
                "color": "#fff8e1",
                "tasks": [
                    {"id": str(uuid.uuid4()), "name": "Drone Data Collection", "assignee": "", "status": "Not Started", "notes": "", "duration": "1 hour"},
                    {"id": str(uuid.uuid4()), "name": "File Organization & Labeling", "assignee": "", "status": "Not Started", "notes": "", "duration": "2 hours"},
                    {"id": str(uuid.uuid4()), "name": "Pilot Access to InsightEye.AI Dashboard", "assignee": "", "status": "Not Started", "notes": "", "duration": "0.5 hours"},
                    {"id": str(uuid.uuid4()), "name": "Upload to GCP Bucket", "assignee": "", "status": "Not Started", "notes": "", "duration": "3 hours"},
                    {"id": str(uuid.uuid4()), "name": "Upload Confirmation", "assignee": "", "status": "Not Started", "notes": "", "duration": "0.5 hours"},
                    {"id": str(uuid.uuid4()), "name": "Automated Upload Notification", "assignee": "", "status": "Not Started", "notes": "", "duration": "0.5 hours"}
                ]
            },
            {
                "phase_id": "phase4",
                "phase_name": "Data Processing",
                "color": "#f3e5f5",
                "tasks": [
                    {"id": str(uuid.uuid4()), "name": "Pipeline Initiation", "assignee": "", "status": "Not Started", "notes": "", "duration": "1 hour"},
                    {"id": str(uuid.uuid4()), "name": "Video Extraction & Frame Parsing", "assignee": "", "status": "Not Started", "notes": "", "duration": "4 hours"},
                    {"id": str(uuid.uuid4()), "name": "RGB Processing: Soiling Analysis", "assignee": "", "status": "Not Started", "notes": "", "duration": "6 hours"},
                    {"id": str(uuid.uuid4()), "name": "Thermal Processing: Defect Detection", "assignee": "", "status": "Not Started", "notes": "", "duration": "8 hours"},
                    {"id": str(uuid.uuid4()), "name": "Geolocation Data Extraction", "assignee": "", "status": "Not Started", "notes": "", "duration": "3 hours"},
                    {"id": str(uuid.uuid4()), "name": "AI Model Processing", "assignee": "", "status": "Not Started", "notes": "", "duration": "6 hours"},
                    {"id": str(uuid.uuid4()), "name": "Defect Classification & Validation", "assignee": "", "status": "Not Started", "notes": "", "duration": "4 hours"},
                    {"id": str(uuid.uuid4()), "name": "Results Database Storage", "assignee": "", "status": "Not Started", "notes": "", "duration": "2 hours"}
                ]
            },
            {
                "phase_id": "phase5",
                "phase_name": "Analysis & Reporting",
                "color": "#fce4ec",
                "tasks": [
                    {"id": str(uuid.uuid4()), "name": "Data Compilation & Statistics", "assignee": "", "status": "Not Started", "notes": "", "duration": "3 hours"},
                    {"id": str(uuid.uuid4()), "name": "Defect Distribution Analysis", "assignee": "", "status": "Not Started", "notes": "", "duration": "4 hours"},
                    {"id": str(uuid.uuid4()), "name": "Severity Classification", "assignee": "", "status": "Not Started", "notes": "", "duration": "2 hours"},
                    {"id": str(uuid.uuid4()), "name": "Maintenance Recommendation Generation", "assignee": "", "status": "Not Started", "notes": "", "duration": "3 hours"},
                    {"id": str(uuid.uuid4()), "name": "Report Generation", "assignee": "", "status": "Not Started", "notes": "", "duration": "6 hours"},
                    {"id": str(uuid.uuid4()), "name": "Quality Assurance Review", "assignee": "", "status": "Not Started", "notes": "", "duration": "2 hours"},
                    {"id": str(uuid.uuid4()), "name": "Client Dashboard Update", "assignee": "", "status": "Not Started", "notes": "", "duration": "3 hours"},
                    {"id": str(uuid.uuid4()), "name": "Final Report Delivery", "assignee": "", "status": "Not Started", "notes": "", "duration": "1 hour"}
                ]
            }
        ]
    
    def create_ui(self):
        # Main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title frame
        self.title_frame = ttk.Frame(self.main_frame)
        self.title_frame.pack(fill=tk.X)
        
        self.title_label = ttk.Label(self.title_frame, text="InsightEye.AI Drone Inspection Tracker", 
                                    font=("Arial", 16, "bold"))
        self.title_label.pack(side=tk.LEFT, pady=10)
        
        # Projects frame
        self.projects_frame = ttk.LabelFrame(self.main_frame, text="Projects")
        self.projects_frame.pack(fill=tk.X, pady=10)
        
        self.project_selection_frame = ttk.Frame(self.projects_frame)
        self.project_selection_frame.pack(fill=tk.X, expand=True, padx=5, pady=5)
        
        self.project_label = ttk.Label(self.project_selection_frame, text="Select Project:")
        self.project_label.pack(side=tk.LEFT, padx=5)
        
        self.project_var = tk.StringVar()
        self.project_combo = ttk.Combobox(self.project_selection_frame, textvariable=self.project_var, 
                                        state="readonly", width=40)
        self.project_combo.pack(side=tk.LEFT, padx=5)
        self.update_project_combo()
        self.project_combo.bind("<<ComboboxSelected>>", self.on_project_selected)
        
        self.new_project_btn = ttk.Button(self.project_selection_frame, text="New Project", 
                                        command=self.create_new_project)
        self.new_project_btn.pack(side=tk.LEFT, padx=5)
        
        self.project_details_frame = ttk.Frame(self.projects_frame)
        self.project_details_frame.pack(fill=tk.X, expand=True, padx=5, pady=5)
        
        # Project details placeholders
        self.client_label = ttk.Label(self.project_details_frame, text="Client: ")
        self.client_label.grid(row=0, column=0, sticky=tk.W, padx=5)
        
        self.site_label = ttk.Label(self.project_details_frame, text="Site: ")
        self.site_label.grid(row=0, column=1, sticky=tk.W, padx=5)
        
        self.date_label = ttk.Label(self.project_details_frame, text="Date: ")
        self.date_label.grid(row=1, column=0, sticky=tk.W, padx=5)
        
        self.status_label = ttk.Label(self.project_details_frame, text="Status: ")
        self.status_label.grid(row=1, column=1, sticky=tk.W, padx=5)
        
        # Task management frame
        self.tasks_frame = ttk.LabelFrame(self.main_frame, text="Task Management")
        self.tasks_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create notebook for phases
        self.phase_notebook = ttk.Notebook(self.tasks_frame)
        self.phase_notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Progress frame
        self.progress_frame = ttk.LabelFrame(self.main_frame, text="Project Progress")
        self.progress_frame.pack(fill=tk.X, pady=10)
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress_bar.pack(fill=tk.X, padx=10, pady=10)
        
        self.progress_label = ttk.Label(self.progress_frame, text="Overall Progress: 0%")
        self.progress_label.pack(padx=10, pady=5)
        
        # Status counts
        self.status_frame = ttk.Frame(self.progress_frame)
        self.status_frame.pack(fill=tk.X, padx=10, pady=5)
        
        statuses = ["Not Started", "In Progress", "Completed", "Blocked"]
        colors = ["#f0f0f0", "#fff8e1", "#e8f5e9", "#ffebee"]
        
        for i, status in enumerate(statuses):
            frame = ttk.Frame(self.status_frame, style=f"{status}.TFrame")
            frame.grid(row=0, column=i, padx=5)
            
            label = ttk.Label(frame, text=f"{status}: 0", width=15, anchor=tk.CENTER,
                             background=colors[i])
            label.pack(padx=2, pady=2)
            
        # Bottom buttons frame
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.pack(fill=tk.X, pady=10)
        
        self.refresh_btn = ttk.Button(self.buttons_frame, text="Refresh", command=self.refresh_project)
        self.refresh_btn.pack(side=tk.LEFT, padx=5)
        
        self.save_btn = ttk.Button(self.buttons_frame, text="Save Changes", command=self.save_data)
        self.save_btn.pack(side=tk.LEFT, padx=5)
        
        self.export_btn = ttk.Button(self.buttons_frame, text="Export Report", command=self.export_report)
        self.export_btn.pack(side=tk.LEFT, padx=5)
        
        # If no projects exist, show message
        if not self.data["projects"]:
            for widget in [self.project_details_frame, self.tasks_frame, self.progress_frame]:
                widget.pack_forget()
            
            msg_frame = ttk.Frame(self.main_frame)
            msg_frame.pack(fill=tk.BOTH, expand=True, pady=50)
            
            msg = ttk.Label(msg_frame, text="No projects exist. Please create a new project.", 
                          font=("Arial", 12))
            msg.pack(pady=20)
    
    def update_project_combo(self):
        project_names = [p["name"] for p in self.data["projects"]]
        self.project_combo["values"] = project_names
        
        if project_names:
            self.project_combo.current(0)
    
    def create_new_project(self):
        # Open a dialog to collect project information
        project_name = simpledialog.askstring("New Project", "Enter project name:")
        if not project_name:
            return
            
        client_name = simpledialog.askstring("New Project", "Enter client name:")
        if not client_name:
            return
            
        site_name = simpledialog.askstring("New Project", "Enter site name:")
        if not site_name:
            return
        
        # Create a new project with template workflow
        new_project = {
            "id": str(uuid.uuid4()),
            "name": project_name,
            "client": client_name,
            "site": site_name,
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "Active",
            "phases": self.create_workflow_template()
        }
        
        self.data["projects"].append(new_project)
        self.save_data()
        self.update_project_combo()
        
        # Set as current project
        self.project_var.set(project_name)
        self.on_project_selected(None)
    
    def on_project_selected(self, event):
        project_name = self.project_var.get()
        self.current_project = next((p for p in self.data["projects"] if p["name"] == project_name), None)
        
        if self.current_project:
            # Update UI with project details
            self.client_label.config(text=f"Client: {self.current_project['client']}")
            self.site_label.config(text=f"Site: {self.current_project['site']}")
            self.date_label.config(text=f"Date: {self.current_project['created_date']}")
            self.status_label.config(text=f"Status: {self.current_project['status']}")
            
            # Ensure all UI components are visible
            for widget in [self.project_details_frame, self.tasks_frame, self.progress_frame]:
                widget.pack(fill=tk.X if widget != self.tasks_frame else tk.BOTH, 
                           expand=True if widget == self.tasks_frame else False, pady=10)
            
            # Create phase tabs
            self.refresh_phases()
            
            # Update progress
            self.update_progress()
    
    def refresh_phases(self):
        # Clear existing tabs
        for tab in self.phase_notebook.tabs():
            self.phase_notebook.forget(tab)
        
        # Create new tabs for each phase
        for phase in self.current_project["phases"]:
            frame = ttk.Frame(self.phase_notebook)
            self.phase_notebook.add(frame, text=phase["phase_name"])
            
            # Create task list
            self.create_task_list(frame, phase)
    
    def create_task_list(self, parent_frame, phase):
        # Task list with columns
        columns = ("name", "assignee", "status", "duration", "notes")
        tree = ttk.Treeview(parent_frame, columns=columns, show="headings")
        
        # Define column headings
        tree.heading("name", text="Task Name")
        tree.heading("assignee", text="Assigned To")
        tree.heading("status", text="Status")
        tree.heading("duration", text="Duration")
        tree.heading("notes", text="Notes")
        
        # Define column widths
        tree.column("name", width=250)
        tree.column("assignee", width=150)
        tree.column("status", width=100)
        tree.column("duration", width=80)
        tree.column("notes", width=250)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(parent_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        
        # Pack components
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add tasks to tree
        for task in phase["tasks"]:
            tree.insert("", tk.END, values=(
                task["name"], 
                task["assignee"], 
                task["status"], 
                task["duration"],
                task["notes"]
            ), tags=(task["status"],))
        
        # Configure tags for status colors
        tree.tag_configure("Not Started", background="#f0f0f0")
        tree.tag_configure("In Progress", background="#fff8e1")
        tree.tag_configure("Completed", background="#e8f5e9")
        tree.tag_configure("Blocked", background="#ffebee")
        
        # Add double-click binding to edit task
        tree.bind("<Double-1>", lambda event, ph=phase, tr=tree: self.edit_task(event, ph, tr))
        
        # Add right-click menu
        self.create_context_menu(tree, phase)
    
    def create_context_menu(self, tree, phase):
        menu = tk.Menu(tree, tearoff=0)
        
        def show_menu(event):
            item = tree.identify_row(event.y)
            if item:
                tree.selection_set(item)
                menu.post(event.x_root, event.y_root)
        
        menu.add_command(label="Edit Task", 
                         command=lambda: self.edit_task(None, phase, tree, from_menu=True))
        menu.add_command(label="Assign Task", 
                         command=lambda: self.assign_task(phase, tree))
        menu.add_command(label="Change Status", 
                         command=lambda: self.change_status(phase, tree))
        menu.add_separator()
        menu.add_command(label="Add Note", 
                         command=lambda: self.add_note(phase, tree))
        
        tree.bind("<Button-3>", show_menu)
    
    def edit_task(self, event, phase, tree, from_menu=False):
        if not from_menu:
            # Get the item that was clicked
            item = tree.identify_row(event.y)
            if not item:
                return
            tree.selection_set(item)
        
        # Get selected item
        selected_item = tree.selection()
        if not selected_item:
            return
        
        # Get task values
        item_values = tree.item(selected_item, "values")
        task_name = item_values[0]
        
        # Find the task in the phase
        task = next((t for t in phase["tasks"] if t["name"] == task_name), None)
        if not task:
            return
        
        # Create edit dialog
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit Task: {task_name}")
        edit_window.geometry("500x350")
        edit_window.resizable(False, False)
        edit_window.transient(self.root)
        edit_window.grab_set()
        
        # Create form fields
        ttk.Label(edit_window, text="Task Name:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        name_var = tk.StringVar(value=task["name"])
        name_entry = ttk.Entry(edit_window, textvariable=name_var, width=40)
        name_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        
        ttk.Label(edit_window, text="Assigned To:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        assignee_var = tk.StringVar(value=task["assignee"])
        assignee_combo = ttk.Combobox(edit_window, textvariable=assignee_var, 
                                    values=self.team_members, width=38)
        assignee_combo.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        
        ttk.Label(edit_window, text="Status:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        status_var = tk.StringVar(value=task["status"])
        status_combo = ttk.Combobox(edit_window, textvariable=status_var, 
                                   values=["Not Started", "In Progress", "Completed", "Blocked"], 
                                   width=38)
        status_combo.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        
        ttk.Label(edit_window, text="Duration:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        duration_var = tk.StringVar(value=task["duration"])
        duration_entry = ttk.Entry(edit_window, textvariable=duration_var, width=40)
        duration_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)
        
        ttk.Label(edit_window, text="Notes:").grid(row=4, column=0, padx=10, pady=10, sticky=tk.NW)
        notes_text = tk.Text(edit_window, width=30, height=5)
        notes_text.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)
        notes_text.insert(tk.END, task["notes"])
        
        # Buttons
        def save_changes():
            task["name"] = name_var.get()
            task["assignee"] = assignee_var.get()
            task["status"] = status_var.get()
            task["duration"] = duration_var.get()
            task["notes"] = notes_text.get("1.0", tk.END).strip()
            
            # Update tree view
            tree.item(selected_item, values=(
                task["name"], 
                task["assignee"], 
                task["status"], 
                task["duration"],
                task["notes"]
            ), tags=(task["status"],))
            
            # Update progress
            self.update_progress()
            
            # Close dialog
            edit_window.destroy()
        
        def cancel():
            edit_window.destroy()
        
        button_frame = ttk.Frame(edit_window)
        button_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Save Changes", command=save_changes).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Cancel", command=cancel).pack(side=tk.LEFT, padx=10)
    
    def assign_task(self, phase, tree):
        selected_item = tree.selection()
        if not selected_item:
            return
        
        # Get task values
        item_values = tree.item(selected_item, "values")
        task_name = item_values[0]
        
        # Find the task in the phase
        task = next((t for t in phase["tasks"] if t["name"] == task_name), None)
        if not task:
            return
        
        # Ask for assignee
        assignee = simpledialog.askstring("Assign Task", "Enter assignee name:", 
                                        initialvalue=task["assignee"])
        if assignee is not None:
            task["assignee"] = assignee
            
            # Update tree view
            new_values = list(item_values)
            new_values[1] = assignee
            tree.item(selected_item, values=new_values)
    
    def change_status(self, phase, tree):
        selected_item = tree.selection()
        if not selected_item:
            return
        
        # Get task values
        item_values = tree.item(selected_item, "values")
        task_name = item_values[0]
        
        # Find the task in the phase
        task = next((t for t in phase["tasks"] if t["name"] == task_name), None)
        if not task:
            return
        
        # Create status dialog
        status_window = tk.Toplevel(self.root)
        status_window.title(f"Change Status: {task_name}")
        status_window.geometry("300x200")
        status_window.resizable(False, False)
        status_window.transient(self.root)
        status_window.grab_set()
        
        ttk.Label(status_window, text="Select New Status:").pack(pady=10)
        
        status_var = tk.StringVar(value=task["status"])
        
        for status in ["Not Started", "In Progress", "Completed", "Blocked"]:
            ttk.Radiobutton(status_window, text=status, variable=status_var, 
                          value=status).pack(anchor=tk.W, padx=20, pady=5)
        
        def save_status():
            task["status"] = status_var.get()
            
            # Update tree view
            new_values = list(item_values)
            new_values[2] = status_var.get()
            tree.item(selected_item, values=new_values, tags=(status_var.get(),))
            
            # Update progress
            self.update_progress()
            
            # Close dialog
            status_window.destroy()
        
        ttk.Button(status_window, text="Save", command=save_status).pack(pady=10)
    
    def add_note(self, phase, tree):
        selected_item = tree.selection()
        if not selected_item:
            return
        
        # Get task values
        item_values = tree.item(selected_item, "values")
        task_name = item_values[0]
        
        # Find the task in the phase
        task = next((t for t in phase["tasks"] if t["name"] == task_name), None)
        if not task:
            return
        
        # Create note dialog
        note_window = tk.Toplevel(self.root)
        note_window.title(f"Add Note: {task_name}")
        note_window.geometry("400x250")
        note_window.resizable(False, False)
        note_window.transient(self.root)
        note_window.grab_set()
        
        ttk.Label(note_window, text="Enter Note:").pack(pady=10)
        
        notes_text = tk.Text(note_window, width=45, height=8)
        notes_text.pack(padx=10, pady=5)
        notes_text.insert(tk.END, task["notes"])
        
        def save_note():
            task["notes"] = notes_text.get("1.0", tk.END).strip()
            
            # Update tree view
            new_values = list(item_values)
            new_values[4] = task["notes"]
            tree.item(selected_item, values=new_values)
            
            # Close dialog
            note_window.destroy()
        
        ttk.Button(note_window, text="Save", command=save_note).pack(pady=10)
    
    def update_progress(self):
        if not self.current_project:
            return
        
        # Count tasks by status
        total_tasks = 0
        completed_tasks = 0
        status_counts = {"Not Started": 0, "In Progress": 0, "Completed": 0, "Blocked": 0}
        
        for phase in self.current_project["phases"]:
            for task in phase["tasks"]:
                total_tasks += 1
                if task["status"] in status_counts:
                    status_counts[task["status"]] += 1
                if task["status"] == "Completed":
                    completed_tasks += 1
        
        # Calculate progress percentage
        progress_pct = 0
        if total_tasks > 0:
            progress_pct = int((completed_tasks / total_tasks) * 100)
        
        # Update progress bar
        self.progress_bar["value"] = progress_pct
        self.progress_label.config(text=f"Overall Progress: {progress_pct}%")
        
        # Update status counts
        for i, (status, count) in enumerate(status_counts.items()):
            label = self.status_frame.winfo_children()[i].winfo_children()[0]
            label.config(text=f"{status}: {count}")

    def refresh_project(self):
        if not self.current_project:
            return
        
        # Reload current project (useful if multiple users are editing)
        self.load_data()
        
        # Find the current project again
        project_name = self.project_var.get()
        self.current_project = next((p for p in self.data["projects"] if p["name"] == project_name), None)
        
        if self.current_project:
            # Refresh UI
            self.refresh_phases()
            self.update_progress()
            messagebox.showinfo("Refresh", "Project data refreshed successfully.")
        else:
            messagebox.showerror("Error", "Project not found in updated data.")

    def export_report(self):
        if not self.current_project:
            messagebox.showinfo("Export", "Please select a project first.")
            return
        
        try:
            # Create report filename
            filename = f"{self.current_project['name'].replace(' ', '_')}_report.txt"
            
            with open(filename, 'w') as file:
                # Write header
                file.write(f"InsightEye.AI Drone Inspection Report\n")
                file.write(f"={'='*40}=\n\n")
                
                # Project details
                file.write(f"Project: {self.current_project['name']}\n")
                file.write(f"Client: {self.current_project['client']}\n")
                file.write(f"Site: {self.current_project['site']}\n")
                file.write(f"Date: {self.current_project['created_date']}\n")
                file.write(f"Status: {self.current_project['status']}\n\n")
                
                # Progress summary
                total_tasks = 0
                completed_tasks = 0
                status_counts = {"Not Started": 0, "In Progress": 0, "Completed": 0, "Blocked": 0}
                
                for phase in self.current_project["phases"]:
                    for task in phase["tasks"]:
                        total_tasks += 1
                        if task["status"] in status_counts:
                            status_counts[task["status"]] += 1
                        if task["status"] == "Completed":
                            completed_tasks += 1
                
                progress_pct = 0
                if total_tasks > 0:
                    progress_pct = int((completed_tasks / total_tasks) * 100)
                
                file.write(f"Progress Summary:\n")
                file.write(f"-----------------\n")
                file.write(f"Overall Progress: {progress_pct}%\n")
                for status, count in status_counts.items():
                    file.write(f"{status}: {count}\n")
                file.write("\n")
                
                # Phase details
                file.write(f"Phase Details:\n")
                file.write(f"=============\n\n")
                
                for phase in self.current_project["phases"]:
                    file.write(f"{phase['phase_name']}:\n")
                    file.write(f"{'-' * len(phase['phase_name'])}\n")
                    
                    for task in phase["tasks"]:
                        file.write(f"Task: {task['name']}\n")
                        file.write(f"  Assigned to: {task['assignee'] or 'Unassigned'}\n")
                        file.write(f"  Status: {task['status']}\n")
                        file.write(f"  Duration: {task['duration']}\n")
                        if task["notes"]:
                            file.write(f"  Notes: {task['notes']}\n")
                        file.write("\n")
                    
                    file.write("\n")
            
            messagebox.showinfo("Export Successful", f"Report exported to {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Error exporting report: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DroneInspectionTracker(root)
    
    # Style configuration
    style = ttk.Style()
    style.configure("TFrame", background="#f5f5f5")
    style.configure("TLabel", background="#f5f5f5")
    style.configure("TLabelframe", background="#f5f5f5")
    style.configure("TLabelframe.Label", background="#f5f5f5", font=("Arial", 10, "bold"))
    
    # Make window resizable
    root.resizable(True, True)
    
    # Center window on screen
    window_width = 1200
    window_height = 750
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    root.mainloop()