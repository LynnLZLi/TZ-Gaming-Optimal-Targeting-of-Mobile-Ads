print("===============================================")
print("Testing for code completeness")
print("===============================================")

if "tz_gaming" not in locals():
    raise NameError("Did you not load the tz_gaming data?")
else:
    ### section I
    if "lr" not in locals():
        raise NameError(
            "Part I: Your code should have a fitted logistic regression model called 'lr'"
        )
    if not hasattr(tz_gaming, "pred_logit"):
        raise NameError("Part I: tz_gaming should have a variable 'pred_logit'")
    if "lr_rnd" not in locals():
        raise NameError(
            "Part I: Your code should have a fitted logistic regression model called 'lr_rnd'"
        )
    if not hasattr(tz_gaming, "pred_rnd"):
        raise NameError("Part I: tz_gaming should have a variable 'pred_rnd'")

    ### section II
    if "lr_mc1" not in locals():
        raise NameError(
            "Part II: Your code should have a fitted logistic regression model called 'lr_mc1'"
        )
    if "lr_mc2" not in locals():
        raise NameError(
            "Part II: Your code should have a fitted logistic regression model called 'lr_mc2'"
        )
    if "lr_mc3" not in locals():
        raise NameError(
            "Part II: Your code should have a fitted logistic regression model called 'lr_mc3'"
        )

    ## section III
    if not hasattr(tz_gaming, "pred_logit_dec"):
        raise NameError("Part III: tz_gaming should have a variable 'pred_logit_dec'")
    if "dec_tab" not in locals():
        raise NameError("Part III: Your code should have a DataFrame called 'dec_tab'")
    elif type(dec_tab) != pd.DataFrame:
        raise NameError("Part III: 'dec_tab' should be a pandas DataFrame")
    elif (
        not hasattr(dec_tab, "nr_impressions")
        or not hasattr(dec_tab, "nr_clicks")
        or not hasattr(dec_tab, "ctr")
    ):
        raise NameError(
            "Part III: 'dec_tab' should have columns 'nr_impressions', 'nr_clicks', and 'ctr'"
        )

    ## section IV
    # if "lift_tab" not in locals():
    #     raise NameError("Part IV: Your code should have a DataFrame called 'lift_tab'")
    # elif type(lift_tab) != pd.DataFrame:
    #     raise NameError("Part IV: 'lift_tab' should be a pandas DataFrame")
    # elif not hasattr(lift_tab, "cum_prop") or not hasattr(lift_tab, "cum_lift"):
    #     raise NameError(
    #         "Part IV: 'lift_tab' should have columns 'cum_prop' and 'cum_list'"
    #     )


    # if "profit_tab" not in locals():
    #     raise NameError(
    #         "Part IV: Your code should have a DataFrame called 'profit_tab'"
    #     )
    # elif type(profit_tab) != pd.DataFrame:
    #     raise NameError("Part IV: 'profit_tab' should be a pandas DataFrame")
    # elif not hasattr(profit_tab, "cum_prop") or not hasattr(profit_tab, "cum_profit"):
    #     raise NameError(
    #         "Part IV: 'profit_tab' should have columns 'cum_prop' and 'cum_profit'"
    #     )

    ## section V
    if "cm_logit" not in locals():
        raise NameError("Part V: Your code should have a DataFrame called 'cm_logit'")
    else:
        if type(cm_logit) != pd.DataFrame:
            raise NameError("Part V: 'cm_logit' should be a pandas DataFrame")
        else:
            if not hasattr(cm_logit, "label"):
                raise NameError("Part V: 'cm_logit' should have a column 'label'")
            elif not all(cm_logit.label == ["TP", "FP", "TN", "FN"]):
                raise NameError(
                    "Part V: 'cm_logit.label' should have values ['TP', 'FP', 'TN', 'FN']"
                )

            if not hasattr(cm_logit, "nr"):
                raise NameError("Part V: 'cm_logit' should have a column 'nr'")
            elif not all([type(t) in [int, float] for t in cm_logit.nr]):
                raise NameError(
                    "Part V: 'cm_logit.nr' values should be of type int or float"
                )

    if "accuracy_logit" not in locals():
        raise NameError("Part V: Your code should have a float called 'accuracy_logit'")
    elif not (
        isinstance(accuracy_logit, np.floating) or isinstance(accuracy_logit, float)
    ):
        raise NameError("Part V: 'accuracy_logit' should be of type int or float")

    if "cm_rnd" not in locals():
        raise NameError("Part V: Your code should have a DataFrame called 'cm_rnd'")
    else:
        if type(cm_rnd) != pd.DataFrame:
            raise NameError("Part V: 'cm_rnd' should be a pandas DataFrame")
        else:
            if not hasattr(cm_rnd, "label"):
                raise NameError("Part V: 'cm_rnd' should have a column 'label'")
            elif not all(cm_rnd.label == ["TP", "FP", "TN", "FN"]):
                raise NameError(
                    "Part V: 'cm_rnd.label' should have values ['TP', 'FP', 'TN', 'FN']"
                )

            if not hasattr(cm_rnd, "nr"):
                raise NameError("Part V: 'cm_rnd' should have a column 'nr'")
            elif not all([type(t) in [int, float] for t in cm_rnd.nr]):
                raise NameError(
                    "Part V: 'cm_rnd.nr' values should be of type int or float"
                )

    if "accuracy_rnd" not in locals():
        raise NameError("Part V: Your code should have a float called 'accuracy_rnd'")
    elif not (isinstance(accuracy_rnd, np.floating) or isinstance(accuracy_rnd, float)):
        raise NameError("Part V: 'accuracy_rnd' should be of type float")

    if "cm_logit_recalc" not in locals():
        raise NameError(
            "Part V: Your code should have a DataFrame called 'cm_logit_recalc'"
        )
    else:
        if type(cm_logit_recalc) != pd.DataFrame:
            raise NameError("Part V: 'cm_logit_recalc' should be a pandas DataFrame")
        else:
            if not hasattr(cm_logit_recalc, "label"):
                raise NameError(
                    "Part V: 'cm_logit_recalc' should have a column 'label'"
                )
            elif not all(cm_logit_recalc.label == ["TP", "FP", "TN", "FN"]):
                raise NameError(
                    "Part V: 'cm_logit_recalc.label' should have values ['TP', 'FP', 'TN', 'FN']"
                )

            if not hasattr(cm_logit_recalc, "nr"):
                raise NameError("Part V: 'cm_logit_recalc' should have a column 'nr'")
            elif not all([type(t) in [int, float] for t in cm_logit_recalc.nr]):
                raise NameError(
                    "Part V: 'cm_logit_recalc.nr' values should be of type int or float"
                )

    if "accuracy_logit_recalc" not in locals():
        raise NameError(
            "Part V: Your code should have a float called 'accuracy_logit_recalc'"
        )
    elif not (
        isinstance(accuracy_logit_recalc, np.floating)
        or isinstance(accuracy_logit_recalc, float)
    ):
        raise NameError(
            "Part V: 'accuracy_logit_recalc' should be of type int or float"
        )

    if "cm_rnd_recalc" not in locals():
        raise NameError(
            "Part V: Your code should have a DataFrame called 'cm_rnd_recalc'"
        )
    else:
        if type(cm_rnd_recalc) != pd.DataFrame:
            raise NameError("Part V: 'cm_rnd_recalc' should be a pandas DataFrame")
        else:
            if not hasattr(cm_rnd_recalc, "label"):
                raise NameError("Part V: 'cm_rnd_recalc' should have a column 'label'")
            elif not all(cm_rnd_recalc.label == ["TP", "FP", "TN", "FN"]):
                raise NameError(
                    "Part V: 'cm_rnd.label_recalc' should have values ['TP', 'FP', 'TN', 'FN']"
                )

            if not hasattr(cm_rnd_recalc, "nr"):
                raise NameError("Part V: 'cm_rnd_recalc' should have a column 'nr'")
            elif not all([type(t) in [int, float] for t in cm_rnd_recalc.nr]):
                raise NameError(
                    "Part V: 'cm_rnd_recalc.nr' values should be of type int or float"
                )

    if "accuracy_rnd_recalc" not in locals():
        raise NameError(
            "Part V: Your code should have a float called 'accuracy_rnd_recalc'"
        )
    elif not (
        isinstance(accuracy_rnd_recalc, np.floating)
        or isinstance(accuracy_rnd_recalc, float)
    ):
        raise NameError("Part V: 'accuracy_rnd_recalc' should be of type float")

    ## section VI
    if not hasattr(tz_gaming, "target_logit"):
        raise NameError("Part VI: tz_gaming should have a variable 'target_logit'")
    if not hasattr(tz_gaming, "target_rnd"):
        raise NameError("Part VI: tz_gaming should have a variable 'target_rnd'")
    if not hasattr(tz_gaming, "target_vneta"):
        raise NameError("Part VI: tz_gaming should have a variable 'target_vneta'")
    if not hasattr(tz_gaming, "target_spam"):
        raise NameError("Part VI: tz_gaming should have a variable 'target_spam'")
    if not hasattr(tz_gaming, "pred_spam"):
        raise NameError("Part VI: tz_gaming should have a variable 'pred_spam'")

    if "mod_perf" not in locals():
        raise NameError("Part VI: Your code should have a DataFrame called 'mod_per'")
    else:
        if type(mod_perf) != pd.DataFrame:
            raise NameError("Part VI: 'mod_perf' should be a pandas DataFrame")
        else:
            if not hasattr(mod_perf, "model"):
                raise NameError("Part VI: 'model' should have a column 'model'")
            elif not all(mod_perf.model == ["logit", "rnd", "vneta", "spam"]):
                raise NameError(
                    "Part VI: 'mod_perf' should have values ['logit', 'rnd', 'vneta', 'spam']"
                )

            if not hasattr(mod_perf, "profit"):
                raise NameError("Part VI: 'mod_perf' should have a column 'profit'")
            elif not all(
                [
                    isinstance(p, float) or (isinstance(p, np.floating))
                    for p in mod_perf.profit
                ]
            ):
                raise NameError(
                    "Part VI: 'profit' values in 'mod_perf' should be of type float"
                )

            if not hasattr(mod_perf, "ROME"):
                raise NameError("Part VI: 'mod_perf' should have a column 'ROME'")
            elif not all(
                [
                    isinstance(p, float) or (isinstance(p, np.floating))
                    for p in mod_perf.ROME
                ]
            ):
                raise NameError(
                    "Part VI: 'ROME' values in 'mod_perf' should be of type float"
                )

    if "mod_perf" not in locals():
        raise NameError("Part VI: Your code should have a DataFrame called 'mod_per'")
    else:
        if type(mod_perf_20M) != pd.DataFrame:
            raise NameError("Part VI: 'mod_perf_20M' should be a pandas DataFrame")
        else:
            if not hasattr(mod_perf_20M, "model"):
                raise NameError("Part VI: 'model' should have a column 'model'")
            elif not all(mod_perf_20M.model == ["logit", "rnd", "vneta", "spam"]):
                raise NameError(
                    "Part VI: 'mod_perf_20M' should have values ['logit', 'rnd', 'vneta', 'spam']"
                )

            if not hasattr(mod_perf_20M, "profit"):
                raise NameError("Part VI: 'mod_perf_20M' should have a column 'profit'")
            elif not all(
                [
                    isinstance(p, float) or (isinstance(p, np.floating))
                    for p in mod_perf_20M.profit
                ]
            ):
                raise NameError(
                    "Part VI: 'profit' values in 'mod_perf_20M' should be of type float"
                )

            if not hasattr(mod_perf_20M, "ROME"):
                raise NameError("Part VI: 'mod_perf_20M' should have a column 'ROME'")
            elif not all(
                [
                    isinstance(p, float) or (isinstance(p, np.floating))
                    for p in mod_perf_20M.ROME
                ]
            ):
                raise NameError(
                    "Part VI: 'ROME' values in 'mod_perf_20M' should be of type float"
                )


print("===============================================")
print("Testing complete")
print("===============================================")
