import ast
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import search_directory
lookup_dict = search_directory.file_system_dict

class LookupDriveEvents(FileSystemEventHandler):
    def on_created(self,event):
        print('on_created :{}'.format(event.src_path))
    def on_deleted(self,event):
        print('on_deleted :{}'.format(event.src_path))
    def on_moved(self,event):
        print('on_moved :{}'.format(event.src_path))

if __name__=='__main__':
    observer=Observer()
    event_handler=LookupDriveEvents()

def lookup(drive):
    observer = Observer()
    event_handler = ExampleHandler(ignore_patterns=['*.tmp','*AppData*','*Temp*','*$*','*ProgramData*','*__*'])  # create event handler
    # set observer to use created handler in directory
    observer.schedule(event_handler=event_handler,path='C:\\',recursive=True)
    observer.start()
    observer.join()
