List1 = ['Notes', 'Documents', 'WorkSpace', 'React', 'Angular', 'Veu', 'Office', 'Public', 'Private', 'Classified', 'General', 'Downloads', 'Word File.doc', 'Excel File.doc']
List2 = ['notes', 'documents', 'workspace', 'react', 'angular', 'veu', 'office', 'public', 'private', 'classified', 'general', 'downloads', 'wordFile', 'excelFile']




print(str(List1).replace(' ','').replace('.doc','').lower())
print(str(List2).lower())

data1 = str(List1).replace(' ','').replace('.doc','').lower()
data2 = str(List2).replace(' ','').lower()

assert data1 == data2
