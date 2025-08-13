class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        
        # Validate pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this instance to all
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        """Return a list of all pets owned by this owner"""
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        """Add a pet to this owner after validating it's a Pet instance"""
        if not isinstance(pet, Pet):
            raise Exception("Must be a Pet instance")
        
        pet.owner = self
    
    def get_sorted_pets(self):
        """Return a sorted list of pets by their names"""
        pets_list = self.pets()
        return sorted(pets_list, key=lambda pet: pet.name)
