def create_diagnostic_event(self, event_data: Dict[str, Any]) -> None:
    try:
        if event_data.get("eventKind") not in ("SWC", "BSW"):
            return

        short_name = event_data.get("shortName", "UnknownEvent")
        aging_threshold = int(event_data.get("aging.threshold", event_data.get("agingCycle", 0)))
        self.create_aging_configuration(event_data)

        # Create event element
        event_elements = self.get_element_container("DiagnosticEvents")
        event = AutosarBase.add_sub_element(event_elements, "DIAGNOSTIC-EVENT")

        AutosarBase.add_sub_element(event, "SHORT-NAME", short_name)
        AutosarBase.add_sub_element(event, "EVENT-KIND", event_data["eventKind"])
        AutosarBase.add_sub_element(event, "AGING-ALLOWED", "true" if aging_threshold > 0 else "false")

        confirmation_threshold = int(event_data.get("confirmationThreshold", FAILURE_THRESHOLD_MIN))
        confirmation_threshold = max(FAILURE_THRESHOLD_MIN, min(confirmation_threshold, FAILURE_THRESHOLD_MAX))
        AutosarBase.add_sub_element(event, "EVENT-FAILURE-CYCLE-COUNTER-THRESHOLD", str(confirmation_threshold))

        AutosarBase.add_sub_element(event, "EVENT-CLEAR-ALLOWED", "ALWAYS")
        AutosarBase.add_sub_element(event, "PRESTORAGE-FREEZE-FRAME", "false")

        # Add CONNECTED-INDICATOR if indicator data is present
        indicator_name = event_data.get("indicatorName")
        behavior = event_data.get("indicatorBehavior")
        healing_cycle = event_data.get("healingCycle")

        if indicator_name and behavior and healing_cycle:
            connected_indicator = AutosarBase.add_sub_element(event, "CONNECTED-INDICATOR")
            AutosarBase.add_sub_element(connected_indicator, "SHORT-NAME", f"{short_name}_ConnectedIndicator")
            AutosarBase.add_sub_element(connected_indicator, "BEHAVIOR", behavior)
            AutosarBase.add_sub_element(
                connected_indicator,
                "HEALING-CYCLE-REF",
                healing_cycle,
                {"DEST": "DEM-OPERATION-CYCLE"}
            )
            AutosarBase.add_sub_element(
                connected_indicator,
                "INDICATOR-REF",
                f"/ARRoot/Dem/Indicators/{indicator_name}",
                {"DEST": "DEM-INDICATOR"}
            )

    except Exception as error:
        logging.error(f"Error creating diagnostic event: {error}")
