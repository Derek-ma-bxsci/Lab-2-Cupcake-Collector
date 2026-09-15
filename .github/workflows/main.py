import pygame
import asyncio  
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Place your game loop inside an async function
async def main():  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # --- Your Game Logic & Drawing Code Here ---
        screen.fill((0, 0, 0)) 
        pygame.display.flip()
        
        await asyncio.sleep(0)  # 3. CRITICAL: Add this at the VERY END of your while loop


asyncio.run(main())  
