#
# PySNMP MIB module UBNT-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/UBNT-MIB
# Produced by pysmi-0.2.2 at Mon May 28 16:11:57 2018
# On host jupiter platform Linux version 4.16.11-1-ARCH by user tj
# Using Python version 2.7.15 (default, May  1 2018, 20:16:04) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, enterprises, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ubntMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 41112, 1))
ubntMIB.setRevisions(('2014-02-27 00:00',))
if mibBuilder.loadTexts: ubntMIB.setLastUpdated('201402270000Z')
if mibBuilder.loadTexts: ubntMIB.setOrganization('Ubiquiti Networks, Inc.')
ubnt = MibIdentifier((1, 3, 6, 1, 4, 1, 41112))
ubntSnmpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 2))
ubntSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 2, 1))
ubntAirosGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 2, 2))
ubntAirFiberGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 2, 3))
ubntEdgeMaxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 2, 4))
ubntUniFiGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 2, 5))
ubntAirVisionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 2, 6))
ubntMFiGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 2, 7))
ubntUniTelGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 2, 8))
ubntAirFIBER = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 3))
ubntEdgeMax = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 5))
ubntUniFi = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 6))
ubntAirVision = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 7))
ubntMFi = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 8))
ubntUniTel = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 9))
ubntORTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 1), )
if mibBuilder.loadTexts: ubntORTable.setStatus('current')
ubntOREntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 1, 1), ).setIndexNames((0, "UBNT-MIB", "ubntORIndex"))
if mibBuilder.loadTexts: ubntOREntry.setStatus('current')
ubntORIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ubntORIndex.setStatus('current')
ubntORID = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntORID.setStatus('current')
ubntORDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntORDescr.setStatus('current')
ubntORInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 41112, 1, 2, 1, 1)).setObjects(("UBNT-MIB", "ubntORID"), ("UBNT-MIB", "ubntORDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ubntORInfoGroup = ubntORInfoGroup.setStatus('current')
ubntORCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 41112, 1, 2, 1, 2)).setObjects(("UBNT-MIB", "ubntORInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ubntORCompliance = ubntORCompliance.setStatus('current')
mibBuilder.exportSymbols("UBNT-MIB", ubntOREntry=ubntOREntry, ubntORTable=ubntORTable, ubntAirVisionGroups=ubntAirVisionGroups, ubntSnmpInfo=ubntSnmpInfo, ubntAirVision=ubntAirVision, ubntSnmpGroups=ubntSnmpGroups, ubntUniTel=ubntUniTel, ubntORIndex=ubntORIndex, ubntAirFIBER=ubntAirFIBER, ubntMIB=ubntMIB, ubntAirFiberGroups=ubntAirFiberGroups, ubntMFiGroups=ubntMFiGroups, PYSNMP_MODULE_ID=ubntMIB, ubntUniFi=ubntUniFi, ubntORInfoGroup=ubntORInfoGroup, ubntAirosGroups=ubntAirosGroups, ubntEdgeMaxGroups=ubntEdgeMaxGroups, ubntORCompliance=ubntORCompliance, ubntEdgeMax=ubntEdgeMax, ubntMFi=ubntMFi, ubntUniFiGroups=ubntUniFiGroups, ubntORDescr=ubntORDescr, ubnt=ubnt, ubntUniTelGroups=ubntUniTelGroups, ubntORID=ubntORID)
