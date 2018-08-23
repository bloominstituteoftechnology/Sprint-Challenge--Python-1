self.collision_count = 0

def mult_hits(self, **kwargs):
    if self.collision_count == 3:
        self.object_list.remove(self)

    if self.collision_count == 2:
        self.color = [255,69,0]
            
    if self.touched_by_ball == True:
        self.color = [255,255,0]
        self.collision_count += 1
    self.touched_by_ball = False

color = []