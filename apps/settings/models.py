from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название сайта"   
    )
    logo = models.ImageField(
        upload_to= 'logo/',
        verbose_name='логотип'
    )
    namber = models.CharField(
        max_length=255,
        verbose_name="номер телефона"
    )
    what_number = models.CharField(
        max_length=255,
        verbose_name="ватпсап номер"
    )
    email = models.EmailField(
        verbose_name="почта"
    )
    work_hours1 = models.CharField(
        max_length=255,
        verbose_name="рабочие время в будние"
    )
    work_hours2 = models.CharField(
        max_length=255,
        verbose_name="рабочие время в выходные"
    )
    twitter = models.URLField(
        verbose_name='Twitter'
    )
    facebook = models.URLField(
        verbose_name='Facebook'
    )
    skype = models.URLField(
        verbose_name='skype'
    )
    instagram = models.URLField(
        verbose_name='instagram'
    )
    linkedin = models.URLField(
        verbose_name='linkedin'
    )
    youtube = models.URLField(
        verbose_name='youtube'
    )
    project= models.CharField(
        max_length=255,
        verbose_name='количкества сделаных проектов'      
    )
    hours_work = models.CharField(
        max_length=255,
        verbose_name='количкества рабочих часов')
    office= models.CharField(
        max_length=255,
        verbose_name='количкества офисов'  )
    clints = models.CharField(
        max_length= 255,
        verbose_name= "количества клиетов"
    )
    video = models.URLField(
        verbose_name='промо ролик'
    )
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = "Настройки"
    
class About(models.Model):
    name = models.CharField(max_length=255,verbose_name='название' )
    disc = models.TextField(verbose_name="описание")
    disk_mission = models.TextField(verbose_name="описание миссии")
    disk_prem = models.TextField(verbose_name="описание преймушества")
    disk_gorent = models.TextField(verbose_name="описание гарантии")
    image = models.ImageField(upload_to='image/', verbose_name='фото' )
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name="О нас"
        verbose_name_plural="О нас"
  
class Employee(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='фото' )
    names = models.CharField(max_length=255, verbose_name='имя сотрудника' )
    rols = models.CharField(max_length=255, verbose_name='роль сотрудника')
    diks = models.TextField(verbose_name='мини описание')
    diks2 = models.TextField(verbose_name='описание')
    name1 = models.CharField(max_length=255, verbose_name='имя сотрудника(для нашей коммандой)')
    rols1 = models.CharField(max_length=255, verbose_name='роль сотрудника')
    photo1 = models.ImageField(upload_to='photo1', verbose_name='фото')
    name2 = models.CharField(max_length=255, verbose_name='имя сотрудника')
    rols2 = models.CharField(max_length=255, verbose_name='роль сотрудника')
    photo2 = models.ImageField(upload_to='photo2', verbose_name='фото')
    name3 = models.CharField(max_length=255, verbose_name='имя сотрудника')
    rols3 = models.CharField(max_length=255, verbose_name='роль сотрудника')
    photo3 = models.ImageField(upload_to='photo3', verbose_name='фото')
    name4 = models.CharField(max_length=255, verbose_name='имя сотрудника')
    rols4 = models.CharField(max_length=255, verbose_name='роль сотрудника')
    photo4 = models.ImageField(upload_to='photo4', verbose_name='фото')




    def __str__(self):
        return f"{self.names}"
    class Meta():
        verbose_name='Cотрудник'
        verbose_name_plural="Сотрудники"


class Slide(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя сайта')
    discriptions = models.CharField(max_length=255, verbose_name='описание')
    photos = models.ImageField(upload_to='photos/', verbose_name='фото')
    def __str__(self):
        return f"{self.name}"
    class Meta():
        verbose_name='слайд'
        verbose_name_plural="слайды"
class Servides(models.Model):
    servides = models.CharField(max_length=255, verbose_name='название услуги')
    dirs = models.CharField(max_length=255, verbose_name='описание')
    def __str__(self):
        return f"{self.servides}"
    class Meta():
        verbose_name='услуга'
        verbose_name_plural="услуги"
class Reviews(models.Model):
    dick = models.TextField(verbose_name='отзыв')
    image = models.ImageField(upload_to='fots/',verbose_name='фото клиента')
    client_name = models.CharField(max_length=255, verbose_name='имя клиента')
    servid = models.CharField(max_length=255, verbose_name='какая услуга')
    def __str__(self):
        return f"{self.client_name}"
    class Meta():
        verbose_name='отзыв'
        verbose_name_plural="отзывы"
        
class Blogs(models.Model):
    photo = models.ImageField(upload_to='phot', verbose_name='фото' )
    name = models.CharField(max_length=255, verbose_name='название поста')
    description = models.CharField(max_length=255, verbose_name='опицание')
    data = models.CharField(max_length=255, verbose_name='день публикатци')
    mount = models.CharField(max_length=255, verbose_name='месяц публикатци')
    def __str__(self):
        return f"{self.name}"
    class Meta():
        verbose_name='пост'
        verbose_name_plural="посты"
        
class Project(models.Model):
    project_name = models.CharField(max_length=255, verbose_name='название проэкта')
    image = models.ImageField(upload_to='proj_photo', verbose_name='фото проэкта')
    disk = models.TextField( verbose_name='описание проекта')
    def __str__(self):
        return f"{self.project_name}"
    class Meta():
        verbose_name='проэкт'
        verbose_name_plural="проэкты"