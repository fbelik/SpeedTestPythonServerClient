import java.net.*
import java.io.*

fun main(args: Array<String>) {
    if (args.size != 3) {
        println("Missing arguments")
        println("kotlin SpeedClientKt [HOST_ADDR] [HOST_PORT] [CHUNKS]")
    }
    else {
        val CHUNK_SIZE = 4194399
        val client = Socket(args[0], args[1].toInt())
        
        val dIS = DataInputStream(client.getInputStream())
        val dOS = DataOutputStream(client.getOutputStream())
 
        val byteBuffer = ByteArray(CHUNK_SIZE)
    
        val CHUNKS = args[2].toInt()
        dOS.writeInt(CHUNKS) // Chunks
        
        println("The server message size is $CHUNK_SIZE")
        println("About to request $CHUNKS chunks of $CHUNK_SIZE bytes")
        println("There will be a '.' printed for every 1 chunks (${CHUNK_SIZE/1000} kbytes) recieved")

        val start = System.currentTimeMillis()

        println("Start time: $start milliseconds")
    
        for (i in 0 until CHUNKS) {
            var ct = 0
            while (ct < CHUNK_SIZE) {
                ct += dIS.read(byteBuffer, ct, CHUNK_SIZE - ct)
            }
            print('.')
        }

        val end =  System.currentTimeMillis()
        println()
        println("End time: $end milliseconds")
        println("It took ${(end-start)/1000} seconds to read ${1.0*CHUNKS*CHUNK_SIZE} bytes for a speed of ${1000.0*CHUNKS*CHUNK_SIZE/(end-start)} bytes/second, ${1.0*CHUNKS*CHUNK_SIZE/((end-start))} kBps, ${1.0*CHUNKS*CHUNK_SIZE/((end-start)*1000)} MBps, ${1.0*CHUNKS*CHUNK_SIZE/((end-start)*1000000)} GBps")
        println("Or, in bits/second, ${8000.0*CHUNKS*CHUNK_SIZE/(end-start)} bits/second, ${8.0*CHUNKS*CHUNK_SIZE/(end-start)} kbps, ${8.0*CHUNKS*CHUNK_SIZE/((end-start)*1000)} Mbps, ${8.0*CHUNKS*CHUNK_SIZE/((end-start)*1000000)} Gbps") 
    }
}
