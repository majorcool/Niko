import pygame

speed = 10
# gravity


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, images, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = images.get("start")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = (x_pos, y_pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.status = "run_1"
        self.jump_time = 0

        self.refresh_rate = 5
        self.refresh_counter = 0
        pass

    def jump(self):
        self.status = "jump"
        pass

    def duck(self):
        self.status = "duck_1"
        pass

    def stand(self):
        self.status = "run_1"
        pass

    def die(self):
        self.status = "die_1"
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def refresh(self):
        if self.status == "jump":  # only show one picture when dino jump
            self.image = self.images.get(self.status)
            pass
        elif self.image == self.images.get(self.status): # always use string ending with "_1" as self.status
            self.image = self.images.get(self.status.replace("1", "2")) # swap pictures to create animation
        else: # "_2"
            self.image = self.images.get(self.status.replace("2", "1"))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.status.find("run") != -1:
            if self.refresh_counter == self.refresh_rate:
                self.refresh()
                self.refresh_counter = 0
            self.refresh_counter += 1

        if self.status.find('jump') != -1:

            if self.jump_time >= 40:
                self.status = "run_1"
                self.jump_time = 0
            if self.jump_time < 20:
                self.rect.bottom -= speed

            else:
                self.rect.bottom += speed
            self.jump_time += 1
            self.refresh()

        if self.status == 'duck':
            pass  # duck
