import tkinter as tk
from tkinter import messagebox, simpledialog

class Page:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class HistoryManager:
    def __init__(self, root):
        self.head = None
        self.current = None
        self.bookmarks = {}  # Dictionary to store bookmarks

        # Main GUI components
        self.root = root
        self.root.title("Browser History Manager")

        # History List
        self.history_list = tk.Listbox(root, height=10, width=50)
        self.history_list.pack()

        # Buttons for navigation and actions
        tk.Button(root, text="Visit New Page", command=self.visit_page).pack(fill=tk.X)
        tk.Button(root, text="Go Back", command=self.go_back).pack(fill=tk.X)
        tk.Button(root, text="Go Forward", command=self.go_forward).pack(fill=tk.X)
        tk.Button(root, text="Bookmark Page", command=self.bookmark_page).pack(fill=tk.X)
        tk.Button(root, text="Go to Bookmark", command=self.go_to_bookmark).pack(fill=tk.X)
        tk.Button(root, text="Search History", command=self.search_history).pack(fill=tk.X)
        tk.Button(root, text="Clear History", command=self.clear_history).pack(fill=tk.X)

    def update_history_view(self):
        """Update the listbox with the current history, highlighting the current page."""
        self.history_list.delete(0, tk.END)
        temp = self.head
        while temp:
            display_text = temp.url
            if temp == self.current:
                display_text += " (current)"
            self.history_list.insert(tk.END, display_text)
            temp = temp.next

    def visit_page(self):
        url = simpledialog.askstring("Visit Page", "Enter URL:")
        if url:
            new_page = Page(url)
            if self.current:
                self.current.next = new_page
                new_page.prev = self.current
            else:
                self.head = new_page
            self.current = new_page
            self.update_history_view()

    def go_back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.update_history_view()
        else:
            messagebox.showinfo("Navigation", "No previous page available.")

    def go_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.update_history_view()
        else:
            messagebox.showinfo("Navigation", "No forward page available.")

    def bookmark_page(self):
        if self.current:
            self.bookmarks[self.current.url] = self.current
            messagebox.showinfo("Bookmark", f"Page bookmarked: {self.current.url}")
        else:
            messagebox.showinfo("Bookmark", "No page to bookmark.")

    def go_to_bookmark(self):
        url = simpledialog.askstring("Go to Bookmark", "Enter bookmark URL:")
        if url in self.bookmarks:
            self.current = self.bookmarks[url]
            self.update_history_view()
        else:
            messagebox.showinfo("Bookmark", "Bookmark not found.")

    def search_history(self):
        search_url = simpledialog.askstring("Search History", "Enter URL to search:")
        if search_url:
            temp = self.head
            found = False
            while temp:
                if search_url in temp.url:
                    messagebox.showinfo("Search", f"Found page: {temp.url}")
                    found = True
                    break
                temp = temp.next
            if not found:
                messagebox.showinfo("Search", "Page not found in history.")

    def clear_history(self):
        self.head = None
        self.current = None
        self.bookmarks.clear()
        self.update_history_view()
        messagebox.showinfo("History", "History cleared.")

# Run the GUI
root = tk.Tk()
app = HistoryManager(root)
root.mainloop()
