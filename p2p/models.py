from django.db import models


class Buy(models.Model):
    """
    Peer-to-peer buy transaction
    """

    STATUS_PROCESSED = "processed"
    STATUS_PROCESSING = "processing"
    STATUS_NOT_PROCESSED = "not_processed"
    STATUS_CHOICES = [
        (STATUS_PROCESSED, "Processed"),
        (STATUS_PROCESSING, "Processing"),
        (STATUS_NOT_PROCESSED, "Not Processed"),
    ]

    buyer = models.ForeignKey(
        "prosumer.Prosumer",
        related_name="buies",
        null=False,
        on_delete=models.PROTECT,
        verbose_name="buyer_fk",
        help_text="Foreign Key of the prosumer that performed the buy operation.",
    )
    closing_time = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name="closing_time",
        help_text="The time at which the seller has stopped the buy operation.",
    )
    opening_time = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name="opening_time",
        help_text="The time at which the seller has started the buy operation.",
    )
    status = models.CharField(
        max_length=255,
        blank=False,
        choices=STATUS_CHOICES,
        verbose_name="trade_status",
        help_text="The trade status of the buy operation.",
    )
    units = models.DecimalField(
        max_digits=30,
        decimal_places=8,
        blank=False,
        null=False,
        verbose_name="units_in_kwh",
        help_text="The amount of units in kWh that is bought by the buyer for the specified unit price.",
    )


class Sell(models.Model):
    """
    Peer-to-peer sell transaction.
    """

    STATUS_PROCESSED = "processed"
    STATUS_PROCESSING = "processing"
    STATUS_NOT_PROCESSED = "not_processed"
    STATUS_CHOICES = [
        (STATUS_PROCESSED, "Processed"),
        (STATUS_PROCESSING, "Processing"),
        (STATUS_NOT_PROCESSED, "Not Processed"),
    ]

    closing_time = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name="closing_time",
        help_text="The time at which the the seller has stopped the sell operation.",
    )
    opening_time = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name="opening_time",
        help_text="The time at which the seller has started the sell operation.",
    )
    seller = models.ForeignKey(
        "prosumer.Prosumer",
        related_name="sells",
        null=False,
        on_delete=models.PROTECT,
        verbose_name="seller_fk",
        help_text="Foreign Key of the prosumer that performed the sell operation.",
    )
    status = models.CharField(
        max_length=255,
        blank=False,
        choices=STATUS_CHOICES,
        default=STATUS_NOT_PROCESSED,
        verbose_name="trade_status",
        help_text="The trade status of this sell operation.",
    )
    unit_price = models.DecimalField(
        max_digits=16,
        decimal_places=10,
        blank=False,
        null=False,
        verbose_name="unit_price_in_local_currency",
        help_text="The price per unit in local currency that is imposed on the amount of units sold in the sell operation.",
    )
    units = models.DecimalField(
        max_digits=30,
        decimal_places=8,
        blank=False,
        null=False,
        verbose_name="units_in_kwh",
        help_text="The amount of units in kWh that is sold by the seller for the specified unit price.",
    )


class Trade(models.Model):
    """
    An atomic trade between two peers belonging to the Vaidyuti P2P network.
    """

    buy = models.ForeignKey(
        "p2p.Buy",
        related_name="trades",
        null=False,
        on_delete=models.PROTECT,
        verbose_name="buy_fk",
        help_text="The buy operation associated with the atomic trade.",
    )
    closing_time = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name="closing_time",
        help_text="The time at which the trade between the two peers has stopped.",
    )
    opening_time = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name="opening_time",
        help_text="The time at which the trade between the two peers has started.",
    )
    sell = models.ForeignKey(
        "p2p.Sell",
        related_name="trades",
        null=False,
        on_delete=models.PROTECT,
        verbose_name="sell_fk",
        help_text="The sell operation associated with the atomic trade.",
    )
    unit_price = models.DecimalField(
        max_digits=16,
        decimal_places=10,
        blank=False,
        null=False,
        verbose_name="unit_price_in_local_currency",
        help_text="The price per unit in local currency that is imposed on the amount of units transferred in the trade.",
    )
    units = models.DecimalField(
        max_digits=30,
        decimal_places=8,
        blank=False,
        null=False,
        verbose_name="units_in_kwh",
        help_text="The amount of units in kWh that has been exchanged from the buyer to the seller in the trade for the specified unit price.",
    )
