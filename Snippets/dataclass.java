@Builder
@Value
public final class Result implements Serializable {
    String nick;
    LocalDateTime date_init;
    LocalDateTime date_end;
    double profit;
    double tax;
    Double balance;
    int inputs;
    List<CustomObjects> inputs_by_month;
    // Keep going...
}
public final class Result implements Serializable {
/** Inmmutable class
     * 
     */
    private static final long serialVersionUID = -916675731077365794L;

    private final String nick;
    private final LocalDateTime date_init;
    private final LocalDateTime date_end;

    private final double profit;
    private final double tax;

    private final Double balance;

    private final int inputs;

    private final List<CustomObjects> inputs_by_month;

    // Keep going...

    // constructor

    Results(String nick, LocalDateTime date_init, LocalDateTime date_end,
            double profit, double tax/* Keep going... */) {
        super();
        this.nick = nick;
        this.date_init = date_init;
        this.date_end = date_end;
        this.profit = profit;
        this.tax = tax;
        /* Keep going... */
    }

    /* getters here */
}