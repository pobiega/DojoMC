## DojoMC

Först måste vi se till att vi har allt som behövs för att utveckla minecraft moddar.

### Behövda program

- [JDK (Java Development Kit) 8 x64](https://ninite.com/jdkx8/)
- [IntelliJ Idea Community](https://www.jetbrains.com/idea/download/)
- [Forge MDK Recommended](http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.12.2-14.23.1.2555/forge-1.12.2-14.23.1.2555-mdk.zip)


### Komma igång
När alla tre behövda program är nerladdade och de första 2 installerade, skapa en ny mapp på ett lättåtkommligt ställe, ex **C:\mcmod** och packa upp MDK-zippen i denna mapp. Denna mappen är från och med nu din projektmapp.

Starta sen en kommandoprompt (enklast är att bara skriva **"cmd"** i adressfältet).

I detta fältet, skriv följande (det kan ta ett par minuter efter varje kommando):
- **gradlew setupDecompWorkspace**
- **gradlew setupDevWorkspace ideaModule**

När detta är klart är det dags att starta IntelliJ och konfigurera vårt projekt.

- Starta IntelliJ
- Välj **Import Project**
- Välj filen **build.gradle** som finns i din projektmapp. Tryck **OK**.
- Tryck bara **OK** i nästa fönster också. Standardinställningarna är bra.
- Öppna **Project Structure** skärmen. Leta efter en ikon i uppe höger hörn som ser ut såhär: ![Project Structure](https://pobiega.github.io/DojoMC/img/project_structure.png)
- Under **Project SDK**, välj **1.8**.
- Under **Project language level**, välj **"SDK Default"**.
- Välj nu **Modules** i menyn till vänster.
- Tryck på det gröna plus-tecknet, välj **Import module**.
- Välj **.iml** filen som ligger i din projektmapp. Den borde ha samma namn som ditt projekt.
- Tryck **OK**. Nu borde du vara tillbaka i huvudskärmen av IntelliJ.
- Vänta tills det inte finns en blå mätare i nedre högra hörnet och stäng sedan ner IntelliJ.

Nu går vi tillbaka till kommandoprompten vi startade tidigare, och kör...
- **gradlew genIntellijRuns**

Vänta tills detta kommandot är klart. Nu kan vi starta IntelliJ igen och börja koda!