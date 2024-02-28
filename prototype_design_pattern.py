from abc import ABC, abstractmethod  # Importing the ABC (Abstract Base Class) module to define abstract classes and methods
from copy import deepcopy  # Importing the deepcopy function to create a deep copy of objects

class DocumentPrototype(ABC):  # Defining an abstract base class for document prototypes
    @abstractmethod
    def clone_document(self):  # Abstract method to clone a document
        pass

    @abstractmethod
    def display(self):  # Abstract method to display the document
        pass

class Document(DocumentPrototype):  # Defining a concrete class for documents that implements the DocumentPrototype
    def __init__(self, content, images, formatting, annotations):  # Constructor to initialize document attributes
        self.content = content  # Content of the document
        self.images = deepcopy(images)  # List of images in the document (deep copied)
        self.formatting = formatting  # Formatting style of the document
        self.annotations = deepcopy(annotations)  # List of annotations in the document (deep copied)

    def clone_document(self):  # Implementation of the clone_document method to create a clone of the document
        return Document(
            self.content,
            self.images,
            self.formatting,
            self.annotations
        )
    
    def display(self):  # Implementation of the display method to print the document's content
        print(f"Content: {self.content}\nImages: {self.images}\nFormatting: {self.formatting}\nAnnotations: {self.annotations}")
    
    def add_image(self, image):  # Method to add an image to the document
        self.images.append(image)

    def add_annotation(self, annotation):  # Method to add an annotation to the document
        self.annotations.append(annotation)


images = ["Image1.png"]  # List of images for the original document
annotations = ["Annotation1"]  # List of annotations for the original document

original_doc = Document(  # Creating the original document object
    "Hello, World!",
    images,
    "Basic",
    annotations
)

# Cloning the document using the prototype pattern
copied_doc = original_doc.clone_document()

# Making changes to the original document
original_doc.add_image("Image2.png")  # Adding another image to the original document
original_doc.add_annotation("Annotation2")  # Adding another annotation to the original document

# Displaying the contents of both documents
print("Original Document:")  # Printing the label for the original document
original_doc.display()  # Displaying the content of the original document
print("\nCopied Document:")  # Printing the label for the copied document
copied_doc.display()  # Displaying the content of the copied document