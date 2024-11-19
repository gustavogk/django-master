from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from cars.models import Car
from django.dispatch import receiver

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance , **kwargs):
    print('Car pre save signal')
    print(instance)

@receiver(post_save, sender=Car)
def car_pre_save(sender, instance , **kwargs):
    print('Car post save signal')
    print(instance)

@receiver(pre_delete, sender=Car)
def car_pre_save(sender, instance , **kwargs):
    print('Car pre delete signal')
    print(instance)

@receiver(post_delete, sender=Car)
def car_pre_save(sender, instance , **kwargs):
    print('Car post delete signal')
    print(instance)