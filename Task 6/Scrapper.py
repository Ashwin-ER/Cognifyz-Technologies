import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

class SimpleWebScraper:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Web Scraper")
        self.root.geometry("900x600")

        self.create_widgets()

    def create_widgets(self):
        # URL Entry
        ttk.Label(self.root, text="Website URL:").pack(pady=5)
        self.url_entry = ttk.Entry(self.root, width=50)
        self.url_entry.pack(pady=5)
        self.url_entry.insert(0, "https://books.toscrape.com/")

        # Scrape Button
        ttk.Button(self.root, text="Scrape Data", command=self.scrape_data).pack(pady=10)

        # Results Frame
        self.results_frame = ttk.Frame(self.root)
        self.results_frame.pack(pady=10, fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.results_frame)
        scrollbar.pack(side="right", fill="y")

        # Treeview for results
        self.tree = ttk.Treeview(self.results_frame,
                               columns=("Content", "Type", "URL"),
                               show="headings",
                               yscrollcommand=scrollbar.set)
        self.tree.pack(fill="both", expand=True)
        
        scrollbar.config(command=self.tree.yview)

        # Configure column headings
        self.tree.heading("Content", text="Content")
        self.tree.heading("Type", text="Content Type")
        self.tree.heading("URL", text="Source URL")
        
        # Configure column widths
        self.tree.column("Content", width=500)
        self.tree.column("Type", width=100)
        self.tree.column("URL", width=200)

        # Status Label
        self.status = ttk.Label(self.root, text="")
        self.status.pack(pady=5)

    def scrape_data(self):
        """Scrape common elements from any website"""
        url = self.url_entry.get()

        if not url:
            messagebox.showwarning("Warning", "Please enter a URL!")
            return

        try:
            # Clear previous results
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Send HTTP request
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Scrape common elements
            elements = []
            
            # Headings (h1-h6)
            for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                elements.extend(soup.find_all(tag))
            
            # Paragraphs
            elements.extend(soup.find_all('p'))
            
            # Links
            elements.extend(soup.find_all('a', href=True))
            
            # List items
            elements.extend(soup.find_all('li'))

            if not elements:
                messagebox.showwarning("Warning", "No meaningful content found on this page!")
                return

            # Process and display each element
            for element in elements:
                content_type = element.name
                content = None
                
                if element.name == 'a':
                    content = f"{element.get_text(strip=True)} ({element['href']})"
                    content_type = "link"
                else:
                    content = element.get_text(strip=True)
                
                if content and content.strip():  # Only add non-empty content
                    self.tree.insert('', 'end', values=(content, content_type, url))

            self.status.config(text=f"Successfully scraped {len(elements)} items")

            # Bind double-click to open URL
            self.tree.bind("<Double-1>", lambda e: self.open_url(url))

        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch website: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def open_url(self, url):
        """Open the URL in browser"""
        webbrowser.open(url)

def main():
    root = tk.Tk()
    app = SimpleWebScraper(root)
    root.mainloop()

if __name__ == "__main__":
    main()
