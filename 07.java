import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.Comparator;

public class Day7 {
    static record Hands(String card, long bid, long type, long value) {}
    static long type(String line, boolean p2) {
        char[] hand = new char['T'+1];
        int jokers = 0, ret = 0, max = '2';
        for (char card : line.toCharArray()) {
            if (p2 && card == 'J') {
                jokers++;
                continue;
            }
            if (++hand[card] > hand[max]) {
                max = card;
            }
        }
        hand[max] += jokers;
        for (int i : hand) {
            hand[i]++;
        }
        for (int i = 5; i >= 1; --i) {
            ret = ret * 10 + hand[i];
        }
        return ret;
    }

    static long value(String line, boolean p2) {
        long ret = 0;
        for (char card : line.toCharArray()) {
            long value = switch (card) {
                case 'T' -> 10;
                case 'J' -> p2 ? 1 : 11;
                case 'Q' -> 12;
                case 'K' -> 13;
                case 'A' -> 14;
                default -> card - 0x30;
            };
            ret = ret * 100 + value;
        }
        return ret;
    }

    public static void main(String[] args) throws IOException {
        for (int part = 0; part < 2; ++part) {
            List<Hands> cards = new ArrayList<>();
            for (String lines : Files.readAllLines(Paths.get("07.txt"))) {
                Scanner scanner = new Scanner(lines);
                String line = scanner.next();
                cards.add(new Hands(line, scanner.nextLong(), type(line, part == 1), value(line, part == 1)));
            }
            cards.sort(Comparator.comparingLong((Hands card) -> card.type).thenComparingLong(card -> card.value));
            long sum = 0;
            int i = 1;
            for (Hands card : cards) {
                sum += card.bid * i++;
            }
            System.out.println(sum);
        }
    }
}
