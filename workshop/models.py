from django.db import models


class collegeverification(models.Model):
    collegename = models.CharField(max_length=100)
    collegecode = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.collegecode


class studentregistration(models.Model):
    college_code = models.ForeignKey(collegeverification, on_delete=models.CASCADE, primary_key=True, unique=True)
    invitation_letter = models.FileField(upload_to='document/invitation/', default='', blank=True)

    leader_name = models.CharField(max_length=50, default='', blank=True)
    leader_id = models.FileField(upload_to='document/studentid/', default='', blank=True)
    leader_mobile = models.CharField(max_length=11, default='', blank=True)
    leader_email = models.EmailField(max_length=50, default='', blank=True)

    member1_name = models.CharField(max_length=50, default='', blank=True)
    member1_id = models.EmailField(max_length=50, default='', blank=True)
    member1_mobile = models.CharField(max_length=11, default='', blank=True)
    member1_file = models.FileField(upload_to='document/studentid/', default='', blank=True)

    member2_name = models.CharField(max_length=50, default='', blank=True)
    member2_id = models.EmailField(max_length=50, default='', blank=True)
    member2_mobile = models.CharField(max_length=11, default='', blank=True)
    member2_file = models.FileField(upload_to='document/studentid/', default='', blank=True)

    member3_name = models.CharField(max_length=50, default='', blank=True)
    member3_id = models.EmailField(max_length=50, default='', blank=True)
    member3_mobile = models.CharField(max_length=11, default='', blank=True)
    member3_file = models.FileField(upload_to='document/studentid/', default='', blank=True)

    member4_name = models.CharField(max_length=50, default='', blank=True)
    member4_id = models.EmailField(max_length=50, default='', blank=True)
    member4_mobile = models.CharField(max_length=11, default='', blank=True)
    member4_file = models.FileField(upload_to='document/studentid/', default='', blank=True)

    def __str__(self):
        return self.college_code.collegecode + " - " + self.college_code.collegename


class contact_us(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    college_name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.college_name


class events(models.Model):
    event_name = models.CharField(max_length=100)
    belongs_to = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    short_url = models.CharField(max_length=100, unique=True)
    event_image = models.FileField(upload_to='event/images/', default='', blank=True)

    def __str__(self):
        return self.event_name


class event_details(models.Model):
    event_name = models.ForeignKey(events, on_delete=models.CASCADE)
    description = models.TextField()
    rules = models.TextField()

    def __str__(self):
        return self.event_name.event_name


class teams(models.Model):
    team_name = models.CharField(max_length=100)
    short_url = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    event_image = models.FileField(upload_to='teams/thumbnail/', default='', blank=True)

    def __str__(self):
        return self.team_name


class team_images(models.Model):
    team_name = models.ForeignKey(teams, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=100)
    image = models.FileField(upload_to='teams/images/', default='', blank=True)

    def __str__(self):
        return self.team_name.team_name


class team_group_image(models.Model):
    team_name = models.ForeignKey(teams, on_delete=models.CASCADE)
    image = models.FileField(upload_to='teams/images/', default='', blank=True)

    def __str__(self):
        return self.team_name.team_name
