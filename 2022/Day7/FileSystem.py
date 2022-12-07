from collections import namedtuple
from uuid import UUID, uuid4

File = namedtuple('File','name size') 

class Folder:
    def __init__(self,name: str, parent: UUID=None):
        self.name = name                     # folder name/label e.g. Folder1
        self.contents: list[File] = []       # list of files
        self.parent: UUID = parent           # UID of parent folder, None for root
        self.children: list[UUID] = []       # list of the UID of all child folders   
        self.total_file_size: int = 0        # size of all the files in this folder
        self.total_folder_size: int = 0      # size of all the files in this folder + size of all child folders


class FileSystem:
    capacity: int = 70000000
    def __init__(self,file_name: str):
        curr_folder_uid: UUID = uuid4()                         # generate uid for current folder (root)
        self.root: UUID = curr_folder_uid                       # root of the filesystem
        self.folders: dict = {curr_folder_uid: Folder('/')}     # a dict where key is a uid and values is a Folder instance
        with open(file_name,'r') as input_file:
            for line in input_file:
                line = line.strip('\n')
                if line.startswith('$ cd'):
                    # move up (to parent), down (to child) or direct to root
                    cd_arg = line[5:]
                    if cd_arg == '..':
                        # move to parent  
                        curr_folder_uid = self.folders[curr_folder_uid].parent
                    elif cd_arg == '/': 
                        # move to root
                        curr_folder_uid = self.root
                    else:
                        # move to applicable child
                        for c in self.folders[curr_folder_uid].children:
                            if self.folders[c].name == cd_arg:
                                curr_folder_uid = c
                                break
                elif line.startswith('$ ls'):       
                    pass        # nothing to do
                else:
                    # populate current Folder
                    if line.startswith('dir'):
                        # create new folder, add to collection and add uid to children of current node
                        new_folder_uid = uuid4()
                        self.folders[new_folder_uid] = Folder(line[4:], curr_folder_uid)
                        self.folders[curr_folder_uid].children.append(new_folder_uid)
                    else:
                        # otherwise populate contents with file details (size and name) and increment total_file_size and total_folder_size
                        file_details= line.split(' ')
                        file_size = int(file_details[0])
                        file_name = file_details[1]
                        self.folders[curr_folder_uid].contents.append(File(file_name,file_size))
                        self.folders[curr_folder_uid].total_file_size += file_size
                        self.folders[curr_folder_uid].total_folder_size += file_size

        # calculate the total size of all folders in tree
        self._calc_total_folder_sizes(self.root)

    def _calc_total_folder_sizes(self,curr_folder_uid: UUID) -> int:
        for c in self.folders[curr_folder_uid].children:
            self.folders[curr_folder_uid].total_folder_size += self._calc_total_folder_sizes(c) 
        return self.folders[curr_folder_uid].total_folder_size

    def total_size_of_folders_up_to_size(self,max_size: int) -> int:
        '''
        Return the total size of all folders with a size no bigger than max_size
        '''
        return sum(map(lambda v: v.total_folder_size if v.total_folder_size <= max_size else 0, self.folders.values()))
        

    def smallest_to_delete(self,free_space_required: int) -> int:
        '''
        Find the smallest folder you can delete to free up enough space for update
        Return the size of smallest folder
        '''
        space_needed = free_space_required - (FileSystem.capacity - self.folders[self.root].total_folder_size)
        candidates = [v.total_folder_size for v in self.folders.values() if v.total_folder_size >= space_needed]
        return sorted(candidates, key=lambda c: c)[0]

