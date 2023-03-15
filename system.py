"""Abstraction system for KRPC"""
import krpc

conn = krpc.connect()

def getTime():
    return conn.space_center.ut

def getVersion():
    return conn.krpc.get_status().version

def getCurrentVessel():
    return conn.space_center.active_vessel