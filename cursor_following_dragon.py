import pygame
import math

# ---------------- CONFIG ----------------
WIDTH, HEIGHT = 1100, 750
FPS = 60
BG = (0, 0, 0)
BONE = (230, 230, 230)
JOINT = (180, 180, 180)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Walking Skeletal Dragon")
clock = pygame.time.Clock()

# ---------------- DRAGON ----------------
class SkeletalDragon:
    def __init__(self, x, y):
        self.speed = 4
        self.segs = 50
        self.spacing = 9
        self.walk_time = 0

        self.head = pygame.Vector2(x, y)
        self.spine = [pygame.Vector2(x - i * self.spacing, y)
                      for i in range(self.segs)]

        # leg positions
        self.legs = [10, 14, 20, 24]

    def update(self, mx, my):
        target = pygame.Vector2(mx, my)
        d = target - self.head
        dist = d.length()

        if dist > 5:
            d.normalize_ip()
            self.head += d * self.speed
            self.walk_time += 0.2

        self.spine[0] = self.head

        # spine follow
        for i in range(1, self.segs):
            v = self.spine[i] - self.spine[i - 1]
            if v.length() == 0:
                continue
            v.scale_to_length(self.spacing)
            self.spine[i] = self.spine[i - 1] + v

    def draw(self, s):
        # spine
        for i in range(self.segs - 1):
            pygame.draw.line(s, BONE, self.spine[i], self.spine[i + 1], 1)

        for i in range(1, self.segs):
            p = self.spine[i]
            d = self.spine[i - 1] - p
            if d.length() == 0:
                continue
            d.normalize_ip()
            perp = pygame.Vector2(-d.y, d.x)

            # ribs
            if 4 < i < 28:
                size = 18 * (1 - i / 28)
                pygame.draw.line(s, BONE, p, p + perp * size - d * 4, 1)
                pygame.draw.line(s, BONE, p, p - perp * size - d * 4, 1)

            # legs
            if i in self.legs:
                phase = self.walk_time + i
                self.draw_leg(s, p, d, perp, phase, 1)
                self.draw_leg(s, p, d, perp, phase + math.pi, -1)

        self.draw_head(s)
        self.draw_tail(s)

    # ---------------- WALKING LEG ----------------
    def draw_leg(self, s, hip, d, perp, phase, side):
        swing = math.sin(phase) * 6
        lift = abs(math.sin(phase)) * 5

        hip_joint = hip + perp * side * 7
        knee = hip_joint + perp * side * (16 + swing) + d * 8
        ankle = knee + perp * side * (14 + swing) + d * 8
        foot = ankle + d * (10 - lift)

        pygame.draw.line(s, BONE, hip, hip_joint, 1)
        pygame.draw.line(s, BONE, hip_joint, knee, 1)
        pygame.draw.line(s, BONE, knee, ankle, 1)
        pygame.draw.line(s, BONE, ankle, foot, 1)

        pygame.draw.circle(s, JOINT, hip_joint, 3)
        pygame.draw.circle(s, JOINT, knee, 3)
        pygame.draw.circle(s, JOINT, ankle, 2)

    # ---------------- HEAD / SKULL ----------------
    def draw_head(self, s):
        h = self.spine[0]
        d = self.spine[0] - self.spine[1]
        if d.length() == 0:
            return
        d.normalize_ip()
        perp = pygame.Vector2(-d.y, d.x)

        skull_tip = h + d * 20
        jaw = h + d * 14 - perp * 6

        pygame.draw.line(s, BONE, h, skull_tip, 2)
        pygame.draw.line(s, BONE, h, jaw, 1)

        for side in (-1, 1):
            horn_base = h - d * 3 + perp * side * 5
            horn_tip = horn_base - d * 12 + perp * side * 6
            pygame.draw.line(s, BONE, horn_base, horn_tip, 1)

    # ---------------- TAIL ----------------
    def draw_tail(self, s):
        t = self.spine[-1]
        p = self.spine[-2]
        d = t - p
        if d.length() == 0:
            return
        d.normalize_ip()
        perp = pygame.Vector2(-d.y, d.x)

        pygame.draw.line(s, BONE, t, t + d * 18, 1)
        pygame.draw.line(s, BONE, t, t + d * 14 + perp * 6, 1)
        pygame.draw.line(s, BONE, t, t + d * 14 - perp * 6, 1)

# ---------------- MAIN ----------------
dragon = SkeletalDragon(WIDTH // 2, HEIGHT // 2)
running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    mx, my = pygame.mouse.get_pos()
    dragon.update(mx, my)

    screen.fill(BG)
    dragon.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
