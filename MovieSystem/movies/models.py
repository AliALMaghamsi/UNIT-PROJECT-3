from django.db import models
from directors.models import Director
from actors.models import Actor
import json
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    poster=models.ImageField(upload_to="images/movies_posters/")
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.CharField(max_length=200)
    showtime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    seats = models.TextField(default=json.dumps({
        "A1": True, "A2": True, "A3": True, "A4": True, "A5": True, "A6": True,
        "B1": True, "B2": True, "B3": True, "B4": True, "B5": True, "B6": True,
        "C1": True, "C2": True, "C3": True, "C4": True, "C5": True, "C6": True,
        "D1": True, "D2": True, "D3": True, "D4": True, "D5": True, "D6": True,
    }))
    def get_seats(self):
        return json.loads(self.seats)
    
    def update_seat_availability(self, seat_numbers, availability):
        seats = self.get_seats()
        for seat_number in seat_numbers:
            if seat_number in seats:
                seats[seat_number] = availability
        self.seats = json.dumps(seats)
        self.save()

    def __str__(self):
        return f"{self.movie.title} at {self.showtime}"

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    seat_numbers = models.JSONField()  # Stores a list of seat numbers (e.g., ["A1", "A2", "B3"])
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"Ticket {self.id} for {self.screening.movie.title} by {self.user.username}"

