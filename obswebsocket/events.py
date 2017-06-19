#!/usr/bin/env python
# -*- coding: utf-8 -*-

### THIS FILE WAS GENERATED BY ./generate_classes.py - DO NOT EDIT ###

from . import base_classes

class SwitchScenes(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "SwitchScenes"
        self.dataout["scene-name"] = None
        self.dataout["sources"] = None

    def getSceneName(self):
        return self.dataout["scene-name"]

    def getSources(self):
        return self.dataout["sources"]


class ScenesChanged(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "ScenesChanged"


class SourceOrderChanged(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "SourceOrderChanged"
        self.dataout["scene-name"] = None

    def getSceneName(self):
        return self.dataout["scene-name"]


class SceneItemAdded(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "SceneItemAdded"
        self.dataout["scene-name"] = None
        self.dataout["item-name"] = None

    def getSceneName(self):
        return self.dataout["scene-name"]

    def getItemName(self):
        return self.dataout["item-name"]


class SceneItemRemoved(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "SceneItemRemoved"
        self.dataout["scene-name"] = None
        self.dataout["item-name"] = None

    def getSceneName(self):
        return self.dataout["scene-name"]

    def getItemName(self):
        return self.dataout["item-name"]


class SceneItemVisibilityChanged(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "SceneItemVisibilityChanged"
        self.dataout["scene-name"] = None
        self.dataout["item-name"] = None
        self.dataout["item-visible"] = None

    def getSceneName(self):
        return self.dataout["scene-name"]

    def getItemName(self):
        return self.dataout["item-name"]

    def getItemVisible(self):
        return self.dataout["item-visible"]


class SceneCollectionChanged(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "SceneCollectionChanged"


class SceneCollectionListChanged(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "SceneCollectionListChanged"


class SwitchTransition(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "SwitchTransition"
        self.dataout["transition-name"] = None

    def getTransitionName(self):
        return self.dataout["transition-name"]


class TransitionDurationChanged(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "TransitionDurationChanged"
        self.dataout["new-duration"] = None

    def getNewDuration(self):
        return self.dataout["new-duration"]


class TransitionListChanged(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "TransitionListChanged"


class TransitionBegin(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "TransitionBegin"


class PreviewSceneChanged(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "PreviewSceneChanged"
        self.dataout["scene-name"] = None
        self.dataout["sources"] = None

    def getSceneName(self):
        return self.dataout["scene-name"]

    def getSources(self):
        return self.dataout["sources"]


class StudioModeSwitched(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "StudioModeSwitched"
        self.dataout["new-state"] = None

    def getNewState(self):
        return self.dataout["new-state"]


class ProfileChanged(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "ProfileChanged"


class ProfileListChanged(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "ProfileListChanged"


class StreamStarting(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "StreamStarting"
        self.dataout["preview-only"] = None

    def getPreviewOnly(self):
        return self.dataout["preview-only"]


class StreamStarted(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "StreamStarted"


class StreamStopping(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "StreamStopping"
        self.dataout["preview-only"] = None

    def getPreviewOnly(self):
        return self.dataout["preview-only"]


class StreamStopped(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "StreamStopped"


class RecordingStarting(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "RecordingStarting"


class RecordingStarted(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "RecordingStarted"


class RecordingStopping(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "RecordingStopping"


class RecordingStopped(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "RecordingStopped"


class StreamStatus(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "StreamStatus"
        self.dataout["streaming"] = None
        self.dataout["recording"] = None
        self.dataout["preview-only"] = None
        self.dataout["bytes-per-sec"] = None
        self.dataout["kbits-per-sec"] = None
        self.dataout["strain"] = None
        self.dataout["total-stream-time"] = None
        self.dataout["num-total-frames"] = None
        self.dataout["num-dropped-frames"] = None
        self.dataout["fps"] = None

    def getStreaming(self):
        return self.dataout["streaming"]

    def getRecording(self):
        return self.dataout["recording"]

    def getPreviewOnly(self):
        return self.dataout["preview-only"]

    def getBytesPerSec(self):
        return self.dataout["bytes-per-sec"]

    def getKbitsPerSec(self):
        return self.dataout["kbits-per-sec"]

    def getStrain(self):
        return self.dataout["strain"]

    def getTotalStreamTime(self):
        return self.dataout["total-stream-time"]

    def getNumTotalFrames(self):
        return self.dataout["num-total-frames"]

    def getNumDroppedFrames(self):
        return self.dataout["num-dropped-frames"]

    def getFps(self):
        return self.dataout["fps"]


class Exiting(base_classes.BaseEvent):
    def __init__(self):
        base_classes.BaseEvent.__init__(self)
        self.name = "Exiting"


