import kotlin.math.*

fun main(args: Array<String>) {
    val T = readLine()!!.toInt()
    for (case in 1..T) {
        val N = readLine()!!.toInt()
        val list = readLine()!!.split(" ").map(String::toInt)
        var max_val = 0
        list.forEach{a ->
            max_val += max(a, 0)
        }
        var squares:MutableSet<Int> = mutableSetOf()
        var i = 0
        while(i * i <= max_val) {
            squares.add(i * i)
            i += 1
        }
        var cnt = 0
        for (i in 0..N-1) {
            var cum = 0
            list.slice(i..N-1).forEach{
                cum += it
                if (cum in squares) {
                    cnt += 1
                }
            }
        }
        println("Case #" + case.toString() + ": " + cnt.toString())
    }
} 