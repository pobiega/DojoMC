## DojoMC

Först måste vi se till att vi har allt som behövs för att utveckla minecraft moddar.

### Behövda program

- [JDK (Java Development Kit) 8 x64](https://ninite.com/jdkx8/)
- [IntelliJ Idea Community](https://www.jetbrains.com/idea/download/)
- [Forge MDK Recommended](http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.12.2-14.23.1.2555/forge-1.12.2-14.23.1.2555-mdk.zip)


### Komma igång
När alla tre behövda program är nerladdade och de första 2 installerade, skapa en ny mapp på ett lättåtkommligt ställe, ex **C:\mcmod** och packa upp MDK-zippen i denna mapp.

Starta sen en kommandoprompt (enklast är att bara skriva **"cmd"** i adressfältet).

I detta fältet, skriv följande (det kan ta ett par minuter efter varje kommando):
- **gradlew setupDecompWorkspace**
- **gradlew setupDevWorkspace ideaModule**