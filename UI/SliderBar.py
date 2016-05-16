import pygame
class SliderBar:

    def __init__(self):
        self.scrolling = False
        self.maxTimeSlot = 5
        self.currentTimeSlot = 2

    def setValue(self, x, y, width, height):
        self.track = pygame.Rect(x, y, width, height)
        self.knob = pygame.Rect(self.track)
        self.knob.x = self.GetTrackPositionAtTimeSlot(self.currentTimeSlot)
        self.knob.width = self.track.width / self.maxTimeSlot

    def draw_sliderBar(self, surface, trackColor, knobColor, knobBorder):
        pygame.draw.rect(surface, trackColor, (self.track.x, self.track.y, self.track.width, self.track.height), 0)
        pygame.draw.rect(surface, knobBorder, (self.knob.x, self.knob.y, self.knob.width, self.knob.height), 3)
        pygame.draw.rect(surface, knobColor, (self.knob.x, self.knob.y, self.knob.width, self.knob.height), 0)
        return surface

    def IsScrolling(self):
        return  self.scrolling

    def SetScrolling(self, b):
        self.scrolling = b

    def SetMaxTimeSlot(self, _maxTimeSlot):
        self.maxTimeSlot = _maxTimeSlot
        if self.maxTimeSlot == 0:
            self.maxTimeSlot = 1
        self.knob.width = self.track.width / self.maxTimeSlot

    def SetCurrentTimeSlot(self, _currentTimeSlot):
        self.currentTimeSlot = _currentTimeSlot
        self.knob.x = self.currentTimeSlot / self.maxTimeSlot * self.track.width

    def GetTrackPositionAtTimeSlot(self, _timeSlot):
        return _timeSlot / self.maxTimeSlot * self.track.width