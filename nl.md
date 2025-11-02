

# Netlimiter Yama

Close/Quit Netlimiter (NLClientApp.exe -> Task Manager - Details)
and
Stop the associated service NetLimiter Service (nlsvc.exe -> Task Manager - Services)

Open DnSpy.exe v6.1.8 win64bit (12.07.2020) (https://dnspy.org/) as Administrator.
In DnSpy menu - Open the Netlimiter.dll file in its original installation/location (because the library is linked to other dlls) - Remember to make a copy/backup of this file, in case of mishandling.
First Change:

In Explore Assembly window:
plan summary: NetLimiter (version) => NetLimiter.dll => {} NetLimiter.Service => NLLicense -> NLLicense()
Expand Netlimiter (5.3.25), then Netlimiter.dll
Expand Netlimiter.Service
Expand NLLicense
Select NLLicense()

Right click on the code window -> "Edit this method C#"

Replace:
this.IsRegistered = false; -> this.IsRegistered = true;

Click on Compile
Second Change:

In Explore Assembly window:
plan summary: NetLimiter (version) => NetLimiter.dll => {} NetLimiter.Service => NLServiceTemp -> InitLicense ()
Expand Netlimiter (5.3.25), then Netlimiter.dll
Expand Netlimiter.Service
Expand NLServiceTemp
Select InitLicense ()

Right click on the code window -> "Edit this method C#"

Replace:
		DateTime expiration = installTime.AddDays(28.0);
->
		DateTime expiration = installTime.AddDays(99999.0);

Important - To avoid System.Exception error:
(In the same code window - Line 43)

Replace:
catch (Exception exception)
->
catch (System.Exception exception)

Replace here:

		catch (Exception exception)
		{
			regData = null;
			NLServiceTemp._logger.LogError(exception, "Failed to init existing license: {path}", new object[]
			{
				licensePath
			});
		}

->

		catch (System.Exception exception)
		{
			regData = null;
			NLServiceTemp._logger.LogError(exception, "Failed to init existing license: {path}", new object[]
			{
				licensePath
			});
		}

Click on Compile

In DnSpy, Menu - File -> Save All (or Ctrl+Shift+S) -> Click OK

Restart Netlimiter (NLClientApp.exe) and NetLimiter Service (nlsvc.exe)

Update ?
This works for version 5.3.25 but be aware that there may be future changes.

# OPTIONAL: Change Registration Name

In Explore Assembly window:
plan summary: NetLimiter (version) => NetLimiter.dll => {} NetLimiter.Service => NLLicense => RegName ->get_RegName
Expand Netlimiter (5.3.25), then Netlimiter.dll
Expand Netlimiter.Service
Expand NLLicense
Expand RegName
Select get_RegName

Right click on the code window -> "Edit this method C#"

Replace:
return this.<RegName>k__BackingField; -> return "YOURNAMEHERE";

Click on Compile

In DnSpy, Menu - File -> Save All (or Ctrl+Shift+S) -> Click OK
